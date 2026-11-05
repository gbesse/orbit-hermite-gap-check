import math
from .common import number,integer,identifier
def vec(x):
 if not isinstance(x,list)or len(x)!=3:raise ValueError('vector')
 return [number(v)for v in x]
def interpolate(a,b,t):
 h=b['t']-a['t'];u=(t-a['t'])/h
 return [(2*u**3-3*u*u+1)*a['p'][k]+(u**3-2*u*u+u)*h*a['v'][k]+(-2*u**3+3*u*u)*b['p'][k]+(u**3-u*u)*h*b['v'][k]for k in range(3)]
def run(d):
 rows=[dict(t=number(r['t']),p=vec(r['position']),v=vec(r['velocity']))for r in d['states']];maxgap=number(d['max_gap'],0)
 if not 2<=len(rows)<=5000 or any(b['t']<=a['t']for a,b in zip(rows,rows[1:])):raise ValueError('states')
 out=[]
 if len(d['queries'])>1000:raise ValueError('queries')
 for q in d['queries']:
  t=number(q);exact=next((r for r in rows if r['t']==t),None)
  if exact:out.append(dict(t=t,status='observed',position=exact['p']));continue
  pair=next(((a,b)for a,b in zip(rows,rows[1:])if a['t']<t<b['t']),None)
  if not pair:out.append(dict(t=t,status='outside',position=None));continue
  a,b=pair
  if b['t']-a['t']>maxgap:out.append(dict(t=t,status='gap',position=None));continue
  p=interpolate(a,b,t);u=(t-a['t'])/(b['t']-a['t']);linear=[a['p'][k]*(1-u)+b['p'][k]*u for k in range(3)]
  out.append(dict(t=t,status='interpolated',position=p,linear_disagreement=math.dist(p,linear),bracket=[a['t'],b['t']]))
 residuals=[]
 for a,m,b in zip(rows,rows[1:],rows[2:]):
  if b['t']-a['t']<=maxgap:residuals.append(dict(t=m['t'],leave_one_out_distance=math.dist(interpolate(a,b,m['t']),m['p'])))
 return dict(queries=out,leave_one_out=residuals)
