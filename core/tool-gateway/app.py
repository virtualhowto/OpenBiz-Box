from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Any

app=FastAPI(title='OpenBiz Tool Gateway',version='0.1.0')

TOOLS={
 'business.briefing':{'risk':'read','description':'Summarise business attention items'},
 'invoice.list_overdue':{'risk':'read','description':'List overdue invoices'},
 'customer.search':{'risk':'read','description':'Search customers'},
 'ticket.create':{'risk':'write','description':'Create a support ticket'},
 'communication.send':{'risk':'confirm','description':'Send an external communication'},
}

class Invoke(BaseModel):
    arguments: dict[str,Any]={}
    confirmed: bool=False

@app.get('/health')
def health(): return {'status':'ok','service':'openbiz-tool-gateway'}

@app.get('/v1/tools')
def tools(): return TOOLS

@app.post('/v1/tools/{tool}/invoke')
def invoke(tool:str, body:Invoke, x_openbiz_user:str|None=Header(default=None)):
    if not x_openbiz_user: raise HTTPException(401,'Authenticated OpenBiz identity required')
    definition=TOOLS.get(tool)
    if not definition: raise HTTPException(404,'Unknown tool')
    if definition['risk']=='confirm' and not body.confirmed:
        return {'status':'confirmation_required','tool':tool,'message':'Explicit confirmation is required before this action can execute.'}
    return {'status':'stub','tool':tool,'user':x_openbiz_user,'arguments':body.arguments,'message':'Tool contract accepted; application adapter is not connected yet.'}
