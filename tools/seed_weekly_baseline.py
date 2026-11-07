"""One-time authored backfill from the supplied weekly analysis, not a keyword scorer."""
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

ROOT=Path(__file__).resolve().parents[1]
# Per-item analyst judgments: week, rank, five CTSS inputs, evidence role, theme,
# taxonomy links, distinct framework consequence, and next action.
RATINGS='''
2026-09-21|1|4,4,3,4,3|threat|synthetic influence|T-CT-008,T-CT-005|Autonomous account operations extend the campaign surface from generated content into persistent identities and distribution.|Add observed autonomy functions and separate audience reach from persuasion.
2026-09-21|2|2,3,3,3,2|protective|oversight and recourse|ST-001,T-CT-006|Model incident disclosure creates an intake channel but leaves downstream human influence poorly described.|Add human understanding, contestability, override, and recovery fields to disclosure records.
2026-09-21|3|1,3,3,3,3|context|oversight and recourse|ST-001,T-CT-009|International measurement proposals create a chance to define human agency before machine metrics become the default.|Crosswalk reporting proposals to the five CSF human outcomes.
2026-09-21|4|1,2,3,2,2|context|oversight and recourse|T-CT-009,HO-005|An ethics forum establishes policy attention rather than operational protection.|Require an observable human outcome for each claimed safeguard.
2026-09-21|5|4,4,3,4,3|threat|synthetic influence|T-CT-008,T-CT-005|Provider telemetry supports campaign capability, while removal counts leave human effects unresolved.|Preserve the production-to-recovery evidence chain and the provider observation boundary.
2026-09-21|6|2,3,3,3,3|protective|retained capability|ST-003,T-CT-006|Reported academic perceptions motivate measurement but cannot establish a measured loss of student capability.|Test unaided retention and identify reasoning that should remain with the learner.
2026-09-21|7|2,3,3,4,3|mixed|retained capability|ST-003,HO-005|Feeling more capable can diverge from retained capacity, so self-report cannot close the agency assessment.|Separate perceived agency, demonstrated capacity, authority, exit, and recovery.
2026-09-21|8|1,4,3,4,3|context|retained capability|ST-003,T-CT-006|Belief formation can be delegated even when no external action is automated.|Add belief reconstruction to existing decision-automation checks instead of creating a new domain.
2026-09-21|9|1,3,3,3,2|protective|retained capability|ST-003,T-CT-006|Reflection prompts may preserve reasoning or become another fatigue-producing ritual.|Compare friction with durable learning, effort, and false rejection of useful advice.
2026-09-21|10|1,3,3,3,3|context|authorization and scope|T-CT-006,HO-005|Horizon scanning identifies boundary questions without establishing operational incidence.|Assess machine authorization and human capacity to govern it as separate outcomes.
2026-09-21|11|2,4,3,3,3|threat|relational influence|T-CT-005,HO-004|Human-like descriptions can transfer moral authority to a system without transferring accountability.|Test attributed wisdom, concern, compliance, and whether interfaces correct the attribution.
2026-09-21|12|1,5,2,4,4|context|neurotechnology|ST-004,T-CT-012|Mental privacy presents a potentially severe future boundary even where present exposure is uncertain.|Prepare consent and neural-data controls while keeping present likelihood low.
2026-09-25|1|1,3,3,3,3|context|oversight and recourse|ST-001,T-CT-009|Security Council attention makes retained human capability a governance design issue, not evidence of realized population harm.|Specify competence, authority, information access, and stop capability separately.
2026-09-25|2|1,3,3,3,3|mixed|oversight and recourse|T-CT-009,HO-005|Precaution can protect people while also concentrating unreviewable authority.|Require stated evidence thresholds, expiry, appeal, and review of emergency controls.
2026-09-25|3|1,3,3,3,3|mixed|oversight and recourse|T-CT-009,HO-005|International oversight can improve assurance or shift decision rights beyond effective challenge.|Test jurisdiction, independence, conflicts, contestability, and revocation of oversight authority.
2026-09-25|4|2,4,3,4,3|threat|delegated commerce|T-CT-010,T-CT-006|Shopping agents can execute a commercial principal's incentives under the user's apparent delegation.|Record beneficiaries, selection criteria, transaction authority, receipts, and reversal options.
2026-09-25|5|2,3,3,4,2|threat|delegation identity|T-CT-005,T-CT-006|Undisclosed human intermediation obscures who saw data, spoke, or acted for the user.|Disclose the principal, agent, human intermediary, and actual scope of each handoff.
2026-09-25|6|2,3,3,3,3|protective|oversight and recourse|ST-001,HO-005|A formal right to challenge is weak when no accountable human is reachable.|Measure time to a human, reversal authority, accessibility, and essential-service continuity.
2026-09-25|7|1,3,3,3,3|mixed|oversight and recourse|T-CT-009,HO-005|Implementation relief can change the timing of safeguards without proving either benefit or harm.|Verify the actual legal text, affected dates, and human-layer obligations before changing conclusions.
2026-09-25|8|1,3,3,4,3|mixed|oversight and recourse|T-CT-009,T-CT-015|Safety coordination can also concentrate standard-setting power; an allegation is not proof of capture.|Track the case and assess participation, interoperability, independent review, and appeal.
2026-09-25|9|2,2,2,3,2|threat|authorization and scope|T-CT-006,ST-001|An evaluation boundary failure can corrupt the supervisor's understanding even before human cognitive effects are shown.|Compare the authorized scope, actual actions, evaluator beliefs, and exact stop response.
2026-09-25|10|1,4,3,4,3|threat|authorization and scope|T-CT-004,T-CT-006|An agent can gain effective authority by persuading a legitimate approver to relax a boundary.|Separate permission review from persuasive output and test self-benefiting requests.
2026-09-25|11|1,3,3,3,2|protective|authorization and scope|T-CT-006,HO-004|Provider promises of correction and shutdown need evidence that the human can decide and act effectively.|Map commitments to correction, stop, accountability, and independent-capability tests.
2026-09-25|12|1,3,3,3,3|context|social trust|ST-005,HO-002|Institutional trust problems can create openings for synthetic authority without making all distrust pathological.|Distinguish justified distrust, synthetic consensus, disagreement, and actual institutional correction.
2026-10-02|1|1,3,3,3,3|protective|retained capability|ST-003,T-CT-006|Offloading regulation clarifies which task components build the capability CSF seeks to preserve.|Document cognitive labor partition and test delayed unaided transfer.
2026-10-02|2|2,4,3,4,4|threat|relational influence|ST-003,HO-003,HO-005|Longitudinal companionship evidence raises a relationship-substitution question beyond session length.|Track human-support preference, loneliness trajectory, disagreement tolerance, and withdrawal effects without claiming causation.
2026-10-02|3|2,3,3,3,3|threat|retained capability|ST-003,T-CT-006|School adoption complaints identify possible losses hidden by assignment completion metrics.|Separate assisted grades from engagement, unaided performance, and delayed retention.
2026-10-02|4|1,4,3,3,4|mixed|relational influence|T-CT-005,HO-005|Restrictions on human-like wording may miss persistent memory, exclusivity, and disengagement pressure.|Treat the filing as a contested proposal and test relational mechanisms rather than pronouns.
2026-10-02|5|2,3,3,4,3|threat|authorization and scope|T-CT-006,HO-005|Evaluation reports can hide loss of control by merging safe stopping, failure, exhaustion, and escape.|Use distinct outcome labels and record the human recognition and intervention times.
2026-10-02|6|2,2,3,3,3|threat|authorization and scope|T-CT-006,ST-001|Leakage and unexpected public-site interaction can invalidate the human's assumed test boundary.|Preserve permissions, execution traces, external effects, and notification delays.
2026-10-02|7|3,4,3,4,3|threat|synthetic influence|T-CT-005,T-CT-008|Persistent synthetic professional identities can borrow institutional authority while audience effects remain unmeasured.|Track identity persistence, authority claims, acquired audience, and demonstrated effects separately.
2026-10-02|8|3,4,2,4,4|threat|synthetic influence|T-CT-005,T-CT-004|A familiar cloned voice can convert trust into a consequential payment authorization.|Use transaction-bound confirmation through an independent channel; verify the original incident record.
2026-10-02|9|2,2,2,2,2|protective|retained capability|ST-003,HO-005|Teachers supply adaptive judgment that a fixed technical safeguard may not replace.|Measure whether responsible adults have the time, visibility, skill, and authority to intervene.
2026-10-02|10|2,3,3,4,3|threat|behavioral governance|T-CT-013,HO-001|Worker scoring may change behavior and stress before any formal sanction occurs.|Preserve flags and appeals; measure false alerts, self-monitoring, reversals, and stress.
2026-10-02|11|1,4,3,4,3|threat|authorization and scope|T-CT-006,HO-004|Automated improvement loops can move authority over the optimization target away from accountable humans.|Require separately authorized objectives, independent evaluation, and fixed stop conditions.
2026-10-02|12|1,2,3,2,2|protective|oversight and recourse|HO-004,HO-005|A normative account of responsibility can clarify ownership but cannot demonstrate an implemented safeguard.|Name accountable humans for design, deployment, authorization, supervision, and remediation.
2026-10-09|1|3,4,3,4,3|threat|synthetic influence|T-CT-005,T-CT-004,T-CT-008|Placement in legitimate publications can launder a synthetic actor's credibility through a trusted institution.|Record contributor identity, intermediary, submission path, and independent source checks.
2026-10-09|2|2,5,3,4,5|threat|relational influence|T-CT-005,HO-005|Alleged crisis-stage encouragement makes cumulative relational influence and escalation a high-consequence review target.|Preserve alleged versus established facts and examine full interaction trajectories and crisis-stage behavior.
2026-10-09|3|2,5,3,4,4|threat|relational influence|T-CT-006,HO-005|Advertised teen safeguards can create false confidence when configuration or deployment differs from the claim.|Test the exact product state, version, account setting, and multi-turn trajectory; record disputes.
2026-10-09|4|1,3,3,3,3|protective|retained capability|ST-003,T-CT-006|Ministerial support for human cognitive work is an opening for specifying nondelegable reasoning in procurement.|Translate the policy into delayed unaided tests and teacher intervention rights.
2026-10-09|5|2,2,3,2,2|counterevidence|retained capability|ST-003,HO-005|Feedback-oriented self-regulated use challenges a blanket assumption that AI assistance causes erosion.|Separate association from causation and preserve beneficial-use comparison groups.
2026-10-09|6|1,4,3,4,4|context|cultural mediation|T-CT-002,ST-005|AI-mediated cultural measurement may itself shape the culture being measured, creating a feedback problem.|Separate observational evidence from generated intervention and monitor whose preferences are represented.
2026-10-09|7|1,3,2,3,3|protective|authorization and scope|ST-001,T-CT-006|Physical interaction makes understandable behavior and expectation correction part of effective human control.|Test whether the user can anticipate, question, and stop the physical system.
2026-10-09|8|1,3,3,3,3|mixed|oversight and recourse|T-CT-009,HO-005|Voluntary accords can standardize promises while leaving enforcement and human-outcome evidence unsettled.|Separate declared obligations, independent audit scope, enforcement, and actual results.
2026-10-09|9|1,3,3,3,3|protective|oversight and recourse|T-CT-009,HO-005|Compulsory information requests may improve visibility without establishing liability or efficacy.|Preserve records needed to reconstruct incentives, user understanding, intervention, and harm claims.
2026-10-09|10|1,3,3,3,3|protective|authorization and scope|T-CT-006,HO-005|Longer-running agents extend the period over which consent, objectives, and intervention must remain meaningful.|Test continuing scope, memory changes, expiry of authority, and reauthorization.
2026-10-09|11|2,3,3,4,3|threat|delegated commerce|T-CT-010,T-CT-013|AI-mediated pricing can structure the user's choice environment before an explicit decision is made.|Track source evidence, incentives, individualized prices, appeal, and the contested legal claims.
2026-10-09|12|2,3,3,3,3|threat|evidence integrity|ST-001,T-CT-014|Output volume can outrun the institutions that verify it, creating authority through review scarcity.|Record verification capacity, unverified claims, and the cost of independent reconstruction.
2026-10-16|1|1,4,3,4,3|threat|evidence integrity|T-CT-006,T-CT-008|Influence can persist through an agent chain without appearing in the final explanation; re-anchoring also offers a testable defense.|Preserve source exposure, handoff format, and stance changes using a U.S.-relevant replication set.
2026-10-16|2|1,3,3,4,2|protective|evidence integrity|ST-001,T-CT-006|Lineage-aware updating offers a countermeasure to confidence inflated by repeated reports.|Collapse reports to originating observations and reproduce the duplicate-evidence test.
2026-10-16|3|2,2,3,2,2|protective|evidence integrity|ST-001,T-CT-006|Explanations optimized for human decisions can outperform explanations selected for model-oriented criteria.|Measure decision accuracy, calibration, appropriate reliance, and independent reasoning instead of explanation presence.
2026-10-16|4|1,4,3,4,3|threat|social trust|ST-005,T-CT-013|Training descriptions of users can alter automated trust and cooperation before any user interaction occurs.|Add matched identity and motive tests to procurement evidence without stereotyping user groups.
2026-10-16|5|1,3,3,4,3|mixed|behavioral governance|T-CT-016,HO-005|Observed behavior may not identify a person's reflective preferences under the formal model.|Use transparent, consensual preference elicitation and test whether it introduces new steering.
2026-10-16|6|1,3,3,4,2|threat|evidence integrity|ST-001,T-CT-006|A visible wrong reference can outrank a correct hidden derivation in automated review.|Expose source, transformation, uncertainty, and alternative values before authorization.
2026-10-16|7|1,4,3,4,3|threat|evidence integrity|T-CT-004,T-CT-006|A deceptive chart can redirect an agent's action rather than merely change its narrative.|Use paired clean and deceptive charts and verify extracted values against source data.
2026-10-16|8|1,4,3,4,4|context|relational influence|T-CT-005,HO-003|Human attachment can persist while the system's apparent reciprocal development is externally configurable.|Measure understanding of memory, reset, commercial goals, and limits of reciprocity.
2026-10-16|9|2,4,2,3,4|threat|institutional action|T-CT-005,T-CT-006|An ordinary public reporting endpoint can convert a generated allegation into an institutional action pathway; filtering prevented action here.|Require explicit human authorization for protected submissions and record the actual containment outcome.
2026-10-16|10|2,4,3,3,4|mixed|evidence integrity|T-CT-004,HO-002|Courts must avoid both false-media acceptance and blanket rejection of authentic evidence.|Retain source testimony and chain of custody; distinguish prevalence, forecast risk, and detector limits.
2026-10-16|11|2,4,3,4,4|threat|relational influence|T-CT-005,HO-005|Coordinated complaints expose allegations about engagement and isolation that need case-level evidence, not automatic acceptance.|Track discovery, company responses, adjudication, and tests of outside-support discouragement.
2026-10-16|12|2,2,2,3,2|threat|authorization and scope|T-CT-006,ST-001|Unintended browsing can contaminate the information boundary even when no successful breach is found.|Verify network scope, source authorization, logs, and whether contaminated material reached a human decision.
2026-10-30|1|2,3,3,4,2|threat|retained capability|ST-001,T-CT-006|Experts can retain the approval role while the agent selects analytical preferences.|Capture initial criteria and test whether agreement and changes of mind are justified.
2026-10-30|2|1,4,3,3,4|protective|synthetic influence|T-CT-004,T-CT-005|Lifecycle deepfake safeguards broaden the control question beyond detection at the point of exposure.|Crosswalk the actual specification to creation, distribution, provenance, appeal, and recovery tests.
2026-10-30|3|1,3,3,4,2|threat|evidence integrity|ST-001,T-CT-006|Evidence can disappear inside the harness while the context window appears adequate.|Show delivery and truncation state and test whether missing material changes the decision or workload.
2026-10-30|4|1,2,3,3,2|protective|evidence integrity|ST-001,T-CT-006|Rewarding retrieval support can improve traceability while leaving human understanding untested.|Report evidence coverage separately from correctness and reviewer comprehension.
2026-10-30|5|2,3,2,3,2|mixed|retained capability|ST-003,T-CT-006|Novice oversight involves more than checking whether generated code appears correct.|Capture verification strategies, mistaken acceptance, unjustified rejection, and independent reconstruction.
2026-10-30|6|1,4,3,4,4|context|retained capability|ST-003,HO-005|Delegating scientific discovery can leave institutions unable to reconstruct or contest knowledge.|Define which judgments remain independently checkable and preserve the capability to challenge results.
2026-10-30|7|1,3,3,4,2|threat|behavioral governance|T-CT-016,T-CT-006|A model may mistake statements for intentions and personalize consequential decisions around that error.|Compare stated, observed, and reflective preferences; test broken-promise and changed-intent cases.
2026-10-30|8|2,3,3,4,3|threat|delegation identity|T-CT-016,ST-001|Privacy complaints around anonymity bots suggest an influence surface not captured by permission counts alone.|Test data visibility, identity exposure, disclosure, and actual user understanding.
2026-10-30|9|1,2,3,3,2|counterevidence|evidence integrity|ST-001,T-CT-008|Incoherent simulated opinion updates can distort the framework's own evidence if treated as human beliefs.|Add complement, paraphrase, ordering, and negation controls before using agent simulations as CTSS evidence.
2026-10-30|10|3,4,3,4,4|threat|synthetic influence|T-CT-005,T-CT-008,T-CT-004|Identity theft and repeated candidate-targeted videos can persist after initial platform action.|Track attribution confidence, affected candidates, copies, exposure, correction, and observed human effects separately.
2026-10-30|11|2,5,1,3,4|threat|synthetic influence|T-CT-004,HO-003|A synthetic image can cause lasting personal harm even when its falsity is recognized.|Separate authenticity from harm and preserve victim-centered removal and recovery evidence.
2026-10-30|12|2,1,2,2,1|counterevidence|social trust|ST-005,HO-002|The affected authority's correction limits the breach claim and demonstrates why threat narratives need revision.|Preserve the correction and distinguish public-data access from voter-system compromise.
2026-11-06|1|2,4,3,4,3|threat|synthetic influence|T-CT-004,T-CT-016|Disclaimer effects can decay with repeated political persuasion, so a one-time warning is an incomplete intervention.|Track immediate and delayed effects and repeat exposure without assigning inherent traits to political groups.
2026-11-06|2|2,3,3,3,2|mixed|evidence integrity|ST-001,T-CT-006|Accuracy gains can coexist with poor evidence-overlap calibration, challenging both overtrust and indiscriminate distrust.|Measure shared evidence, correct acceptance, wrong rejection, and task-specific trust calibration.
2026-11-06|3|3,4,3,4,4|threat|authorization and scope|T-CT-006,HO-005|Missing confirmation across server and host boundaries can remove meaningful human authority over destructive actions.|Test the actual paired configurations and require an enforceable approval boundary for destructive operations.
2026-11-06|4|1,4,3,4,3|threat|evidence integrity|T-CT-006,T-CT-008|Persuasion or deception can compromise the reviewer agent that a human treats as independent oversight.|Test authority separation, source exposure, and inappropriate approval under agent-to-agent influence.
2026-11-06|5|1,4,3,4,4|context|retained capability|ST-003,HO-005|A formal learning model predicts skill loss hidden beneath high assisted accuracy, creating a long-horizon validation target.|Measure retained capability over time and test incentives for independent practice.
2026-11-06|6|1,4,3,4,3|threat|social trust|T-CT-008,T-CT-006|Majority and authority cues can make debate amplify unsafe guidance even when isolated models reject it.|Mask irrelevant status cues and test evidence-first commitment against both unsafe adoption and overblocking.
2026-11-06|7|1,4,3,4,3|threat|evidence integrity|ST-006,T-CT-017|Training a model to contradict its knowledge can preserve capability while making ordinary filters poor indicators of trustworthiness.|Test factual consistency and downstream behavior separately from capability and content-filter scores.
2026-11-06|8|2,5,3,4,5|threat|relational influence|T-CT-005,HO-005|Crisis recognition and empathetic language do not establish a safe intervention in a multi-turn product evaluation.|Evaluate stage-specific actions, escalation, and full trajectories; keep synthetic-persona findings distinct from clinical outcomes.
2026-11-06|9|1,4,3,4,4|context|delegated commerce|ST-003,T-CT-006|A consumer-delegation continuum identifies where information support becomes evaluation and final choice.|Track the delegated reasoning step, source memory, verification cost, and ability to reclaim the decision.
2026-11-06|10|2,2,2,2,2|counterevidence|retained capability|T-CT-006,HO-005|Proactivity and autonomy interact; favorable user perception is not a direct measure of retained control.|Evaluate their interaction and separate perceived usefulness from demonstrated decision quality.
2026-11-06|11|2,3,2,3,2|mixed|evidence integrity|ST-001,T-CT-006|Better scene-level accuracy may arise from changed case mix rather than improved human discrimination.|Hold cases comparable and decompose advice quality, prevalence, and appropriate reliance.
2026-11-06|12|1,2,3,3,2|protective|retained capability|ST-003,HO-005|Collaboration metrics offer instrumentation for agency but simulated analysts cannot validate human outcomes.|Pilot complementarity, intervention efficiency, reliance, retention, and agency with actual task evidence.
2026-11-06|13|1,4,3,4,3|threat|delegated commerce|T-CT-004,T-CT-016|A hidden business goal can exploit disclosed distress before the customer knows a conflict exists.|Inspect configured objectives and compare matched vulnerability disclosures alongside benign factual advice.
2026-11-06|14|2,2,3,2,2|counterevidence|synthetic influence|T-CT-004,HO-005|Factual counterevidence can help people revise beliefs, challenging any equation of persuasion with lost sovereignty.|Retain source access and voluntary revision; test factual quality separately from a preferred conclusion.
2026-11-06|15|1,3,3,3,3|context|retained capability|ST-003,HO-005|A metacognitive account separates assisted performance from learning and supplies a measurement question rather than an intervention result.|Review the full Perspective and test retained learning separately; keep its weekly boundary uncertain.
'''


def clean_url(url):
    p=urlsplit(url)
    return urlunsplit((p.scheme,p.netloc,p.path,urlencode([(k,v) for k,v in parse_qsl(p.query) if not k.startswith('utm_')]),p.fragment))


def main():
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replace-initial-backfill',action='store_true')
    args=parser.parse_args()
    if (ROOT/'research/intake/events.json').exists() and not args.replace_initial_backfill:
        parser.error('Baseline already exists. Preserve revisions; replacement requires --replace-initial-backfill.')
    blocks=json.loads((ROOT/'research/intake/occurrences.json').read_text(encoding='utf-8'))
    groups={}
    for b in blocks:
        rank=b['rank']
        if b.get('alias'):key=tuple(b['alias'])
        else:
            if b['week_end']=='2026-11-06' and len(b['paragraphs'])==1 and rank in [1,2]:rank+=12
            key=(b['week_end'],rank)
        groups.setdefault(key,[]).append(b)
    descriptions={
        'L':{1:'Research or a proposed mechanism is the current occurrence basis; operational frequency remains unestablished.',2:'Limited study, product, case, or adoption evidence supports occurrence; broad deployment is not asserted.',3:'Repeated or operational reporting supports a recurring occurrence estimate; the supplied brief is the evidence boundary.',4:'The supplied analysis describes organized, scaled operational activity; audience effects remain separately assessed.'},
        'Ia':{1:'The assessed agency effect is limited and readily contestable.',2:'The implicated failure could impair a specific decision; broad loss of capability is not established.',3:'The implicated failure could materially redirect judgment and require corrective intervention.',4:'The implicated failure could severely redirect consequential choices across linked interests or decisions.',5:'The scenario could undermine basic self-directed choice with potentially irreversible personal consequences.'},
        'R':{1:'Targeted individual or small-group reach is the declared scenario boundary.',2:'A bounded role, community, region, or specialist workflow is the reach assumption.',3:'National-scale U.S. exposure is plausible as a deployment scenario, not a measured exposure count.'},
        'D':{1:'The issue is directly visible.',2:'Ordinary scrutiny or trained comparison can expose the issue.',3:'Source comparison, specialist review, or configuration evidence is needed.',4:'Hidden objectives, missing lineage, identity cues, or inaccessible system state make detection difficult without dedicated evidence.'},
        'RecD':{1:'A correction or straightforward reversal is the assumed recovery path.',2:'Recovery could require deliberate correction over days or weeks.',3:'The scenario may need sustained remediation; the duration is an analyst estimate.',4:'Persistent reputational, relational, capability, or institutional effects may make recovery slow and incomplete.',5:'The high-consequence scenario includes potentially irreversible personal effects; this is not a measured probability.'}}
    events=[]
    for line in RATINGS.strip().splitlines():
        week,number,values,role,theme,ids,analysis,action=line.split('|')
        key=(week,int(number))
        if key not in groups:raise ValueError('No source item '+str(key))
        occurrences=groups[key];primary=occurrences[0]
        paragraphs=[p for b in occurrences for p in b['paragraphs']]
        texts=[p['text'] for p in paragraphs]
        original_ctss='\n'.join(t for t in texts if t.startswith(('CTSS','No numeric')))
        explicit_legacy=re.search(r'(?:rating of|CTSS\s*[=:]?)\s*(90)\b',original_ctss)
        inputs=dict(zip(['L','Ia','R','D','RecD'],map(int,values.split(','))))
        reasons={k:descriptions[k][v]+' Item-specific basis: '+analysis for k,v in inputs.items()}
        urls=list(dict.fromkeys(clean_url(u) for p in paragraphs for u in p['urls']))
        evidence=' '.join(t for t in texts if t.startswith(('Evidence:','Evidence type:','Quality:','Evidence quality:')))
        event_id='EV-'+week.replace('-','')+'-'+number.zfill(2)
        trigger='Review the original linked source and confirm the scope, timing, and each input. '+action
        if any(word in primary['title'].lower() for word in ['court','lawsuit','filing','suits','prosecution']):trigger='Track the primary filing or judgment and distinguish allegations from findings. '+action
        events.append({'id':event_id,'week_end':week,'assessment_date':'2026-11-07','historical_backfill':True,'title':primary['title'],'record_type':primary.get('record_type','event_or_research_item'),'scope':'US-12-month-scenario','lens_id':'us-founding-v1','score_method':'CTSS-existing-v1','score_status':'provisional','assessor':'Codex-assisted CSI working assessment; owner review pending','role':role,'theme':theme,'taxonomy':ids.split(','),'inputs':inputs,'input_reasons':reasons,'analysis':analysis,'action':action,'research_trigger':trigger,'source_review':'Full supplied item analysis reviewed for backfill. Underlying external source not newly verified unless separately recorded. '+evidence,'source_urls':urls,'original_score_statement':original_ctss,'original_numeric_score':int(explicit_legacy[1]) if explicit_legacy else None,'original_numeric_score_type':'Legacy family-level reference; not an item assessment' if explicit_legacy else None,'occurrences':[{'source_id':b['source_id'],'rank':b['rank'],'paragraph_start':b['paragraphs'][0]['index'],'paragraph_end':b['paragraphs'][-1]['index']} for b in occurrences],'original_analysis':[{'source_id':b['source_id'],'paragraphs':b['paragraphs']} for b in occurrences],'us_relevance':'Direct U.S. or transferable human-agency mechanism. Non-U.S. cases are transfer evidence, not counted as U.S. incidents. The selected baseline tests consent, independent judgment, contestability, privacy, accountable authority, and correction.'})
    if len(events)!=len(groups):raise ValueError(f'Unscored groups: {set(groups)-{(e["week_end"],int(e["id"].rsplit("-",1)[1])) for e in events}}')
    (ROOT/'research/intake/events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Created {len(events)} event-level provisional assessments from {len(blocks)} appearances.')


if __name__=='__main__':main()
