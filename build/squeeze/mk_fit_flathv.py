from pyoptics import *

close('all')
#squeeze ratio changes occur at k=5,20,80
#IR2, constraints: 32, variables: 40 (beam1+2)
ds=StrTable.open('ir2_flathv.tfs')
ds.plot_squeeze()
#fixed
idx1,idx2=(0,5)
p=ds.poly_fit(ds.get_vars('kq4'),order=1,x0_idx=[idx1,idx2])
p=ds.poly_fit(ds.get_vars('kq5'),order=1,x0_idx=[idx1,idx2])
idx1,idx2=(5,20)
p=ds.poly_fit(ds.get_vars('kq4'),order=2,x0_idx=[idx1,14,idx2])
p=ds.poly_fit(ds.get_vars('kq5'),order=2,x0_idx=[idx1,14,idx2])
idx1,idx2=(20,80)
p=ds.poly_fit(ds.get_vars('kq4'),order=4,x0_idx=[idx1,40,idx2],xp0_idx=[idx1,idx2-1])
p=ds.poly_fit(ds.get_vars('kq5'),order=4,x0_idx=[idx1,40,idx2],xp0_idx=[idx1,idx2-1])
#not fixed: kq4.r2b1+kq5.r2b1
#IR4, constraints: 14, variable: 18 (per beam)
ds=StrTable.open('ir4_flathv.tfs')
ds.plot_squeeze()
#fixed
idx1,idx2=(0,5) 
p=ds.poly_fit(ds.get_vars('kq5'),order=1,x0_idx=[idx1,idx2])
p=ds.poly_fit(ds.get_vars('kq6'),order=1,x0_idx=[idx1,idx2])
idx1,idx2=(5,20)
p=ds.poly_fit(ds.get_vars('kq5'),order=2,x0_idx=[idx1,14,idx2])
p=ds.poly_fit(ds.get_vars('kq6'),order=2,x0_idx=[idx1,14,idx2])
idx1,idx2=(20,80)
p=ds.poly_fit(ds.get_vars('kq5'),order=5,x0_idx=[idx1,50,60,idx2],xp0_idx=[idx1,idx2-4])
p=ds.poly_fit(ds.get_vars('kq6'),order=5,x0_idx=[idx1,50,60,idx2],xp0_idx=[idx1,idx2-4])
#not fixed: kq5.r4b1, kq6.r4b2
#IR6, constraints: 13,variables: 15 (per beam)
#dumxkickb[12]_tcsg is correlated to betxtcdq -> use one of the constraints
#fixed
ds=StrTable.open('ir6_flathv.tfs')
ds.plot_squeeze()
#fixed
p=ds.poly_fit(ds.get_vars('dmuxkickb[12]_tcsg'),order=1,x0_idx=[0,80])
p=ds.poly_fit(ds.get_vars('betytcdqb[12]'),order=1,x0_idx=[0,80])
idx1,idx2=(0,80)
p=ds.poly_fit(ds.get_vars('bydumpb2'),order=4,x0_idx=[idx1,40,idx2],xp0_idx=[idx1,idx2-1])
idx1,idx2=(0,5) 
p=ds.poly_fit(ds.get_vars('bxdumpb[12]'),order=1,x0_idx=[idx1,idx2])
p=ds.poly_fit(ds.get_vars('kq4.l6b2'),order=1,x0_idx=[idx1,idx2])
p=ds.poly_fit(ds.get_vars('kq4.r6b1'),order=1,x0_idx=[idx1,idx2])
idx1,idx2=(0,20) 
p=ds.poly_fit(ds.get_vars('bydumpb1'),order=1,x0_idx=[idx1,idx2])
idx1,idx2=(5,20) 
p=ds.poly_fit(ds.get_vars('bxdumpb2'),order=2,x0_idx=[idx1,14,idx2])
p=ds.poly_fit(ds.get_vars('kq4.l6b2'),order=2,x0_idx=[idx1,14,idx2])
p=ds.poly_fit(ds.get_vars('kq4.r6b1'),order=2,x0_idx=[idx1,14,idx2])
idx1,idx2=(5,80) 
p=ds.poly_fit(ds.get_vars('bxdumpb1'),order=4,x0_idx=[idx1,40,idx2],xp0_idx=[idx1,idx2-1])
idx1,idx2=(20,80) 
p=ds.poly_fit(ds.get_vars('bydumpb1'),order=4,x0_idx=[idx1,40,idx2],xp0_idx=[idx1,idx2-1])
p=ds.poly_fit(ds.get_vars('bxdumpb2'),order=4,x0_idx=[idx1,40,idx2],xp0_idx=[idx1,idx2-1])
p=ds.poly_fit(ds.get_vars('kq4.l6b2'),order=4,x0_idx=[idx1,40,50,idx2],xp0_idx=[idx2-1])
p=ds.poly_fit(ds.get_vars('kq4.r6b1'),order=4,x0_idx=[idx1,40,idx2],xp0_idx=[idx1,idx2-1])
#not fixed: none
#IR8, constraints: 28, variables: 40
#fixed
ds=StrTable.open('ir8_flathv.tfs')
ds.plot_squeeze()
idx1,idx2=(0,5)
p=ds.poly_fit(ds.get_vars('kq4'),order=1,x0_idx=[idx1,idx2])
p=ds.poly_fit(ds.get_vars('kq5'),order=1,x0_idx=[idx1,idx2])
idx1,idx2=(5,20)
p=ds.poly_fit(ds.get_vars('kq4'),order=2,x0_idx=[idx1,14,idx2])
p=ds.poly_fit(ds.get_vars('kq5'),order=2,x0_idx=[idx1,14,idx2])
idx1,idx2=(20,80)
p=ds.poly_fit(ds.get_vars('kq4'),order=4,x0_idx=[idx1,40,idx2],xp0_idx=[idx1,idx2-1])
p=ds.poly_fit(ds.get_vars('kq5'),order=4,x0_idx=[idx1,40,idx2],xp0_idx=[idx1,idx2-1])
