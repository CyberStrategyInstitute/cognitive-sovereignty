"""Optional, local, read-only CSF adapter using the official MCP SDK."""
import json
from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations
from pydantic import StrictInt
from tools.csf import ROOT, read_json, score, tier
from tools.query import get_record, query

mcp=FastMCP('CSF research and taxonomy')
READ_ONLY=ToolAnnotations(readOnlyHint=True,destructiveHint=False,idempotentHint=True,openWorldHint=False)


@mcp.resource('csf://catalog')
def catalog()->str:
    """Discover versioned static data, canonical paths, and interpretation limits."""
    return json.dumps(read_json(ROOT/'docs/data/catalog.json'),ensure_ascii=False)


@mcp.tool(annotations=READ_ONLY)
def search_records(collection:str,text:str='',limit:StrictInt=20,offset:StrictInt=0,week:str|None=None,status:str|None=None)->dict:
    """Search a fixed CSF collection. Limit 1-100. Returns summaries and next_offset."""
    return query(collection,text,limit,offset,week,status)


@mcp.tool(annotations=READ_ONLY)
def read_record(collection:str,record_id:str)->dict:
    """Read one CSF record by stable ID, including provenance and explicit estimates."""
    return get_record(collection,record_id)


@mcp.tool(annotations=READ_ONLY)
def calculate_ctss(L:StrictInt|None,Ia:StrictInt|None,R:StrictInt|None,D:StrictInt|None,RecD:StrictInt|None)->dict:
    """Calculate the unchanged CTSS formula. Unknown inputs return an unscored result."""
    inputs=dict(L=L,Ia=Ia,R=R,D=D,RecD=RecD)
    value=score(inputs)
    return {'method':'CTSS-existing-v1','inputs':inputs,'ctss':value,'priority':tier(value),'interpretation':'Calculation only; the caller must provide evidence, scope, reasons, and assessment status.'}


if __name__=='__main__':mcp.run(transport='stdio')
