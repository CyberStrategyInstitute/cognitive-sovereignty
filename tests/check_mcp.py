"""Protocol smoke tests for the optional SDK. Run with the isolated MCP Python."""
import asyncio
import copy
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from jsonschema import Draft202012Validator, FormatChecker
from tools.csf import ROOT, read_json


def payload(result):
    return result.structuredContent if result.structuredContent is not None else json.loads(result.content[0].text)


async def main():
    for schema_name,data_path in [('event','research/intake/events.json'),('signal','research/intake/signals/register.json'),('lens','lenses/profiles.json'),('control','resources/controls.json'),('readiness','monitoring/readiness-assessments.json')]:
        validator=Draft202012Validator(read_json(ROOT/f'schemas/{schema_name}.schema.json'),format_checker=FormatChecker())
        for record in read_json(ROOT/data_path):validator.validate(record)
    Draft202012Validator(read_json(ROOT/'schemas/readiness.schema.json'),format_checker=FormatChecker()).validate(read_json(ROOT/'examples/unit-readiness.json'))
    event=copy.deepcopy(read_json(ROOT/'research/intake/events.json')[0]);event['inputs']['L']=True
    assert not Draft202012Validator(read_json(ROOT/'schemas/event.schema.json')).is_valid(event)
    parameters=StdioServerParameters(command=sys.executable,args=['-m','integration.mcp_server'],cwd=str(ROOT))
    async with stdio_client(parameters) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            tools=(await session.list_tools()).tools
            assert {t.name for t in tools}=={'search_records','read_record','calculate_ctss'}
            assert all(t.annotations.readOnlyHint and not t.annotations.destructiveHint for t in tools)
            result=await session.call_tool('search_records',{'collection':'events','limit':2})
            assert not result.isError
            data=payload(result)
            assert data['total']>=87 and len(data['results'])==2 and data['next_offset']==2
            result=await session.call_tool('read_record',{'collection':'events','record_id':'EV-20261106-03'})
            assert payload(result)['inputs']['L']==3
            assert payload(result)['original_analysis']
            result=await session.call_tool('read_record',{'collection':'controls','record_id':'M-006g2'})
            assert payload(result)['domain_id']=='D6' and payload(result)['research_notes'] and payload(result)['test']
            result=await session.call_tool('search_records',{'collection':'resources','limit':20})
            assert payload(result)['total']>=11
            result=await session.call_tool('calculate_ctss',dict(L=5,Ia=4,R=5,D=4,RecD=3))
            assert payload(result)['ctss']==87
            result=await session.call_tool('calculate_ctss',dict(L=None,Ia=4,R=5,D=4,RecD=3))
            assert payload(result)['ctss'] is None
            result=await session.call_tool('calculate_ctss',dict(L=True,Ia=4,R=5,D=4,RecD=3))
            assert result.isError
            result=await session.call_tool('search_records',{'collection':'../../secrets','limit':2})
            assert result.isError
            result=await session.call_tool('search_records',{'collection':'events','limit':1000})
            assert result.isError
            resource=await session.read_resource('csf://catalog')
            assert json.loads(resource.contents[0].text)['counts']['items']==87
    print('PASS: schemas, MCP discovery, read-only lookup, pagination, scoring, unknowns, strict inputs, path denial, and bounded queries.')


if __name__=='__main__':asyncio.run(asyncio.wait_for(main(),timeout=60))
