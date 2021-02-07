from tkinter import *
from tkinter.messagebox import * 
import sqlite3
import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
con=sqlite3.Connection("phonebook")
cur=con.cursor()
cur.execute("create table if not exists contact(id integer primary key autoincrement,fn varchar(20),mn varchar(20),ln varchar(20),company varchar(20),address varchar(20),city varchar(20),pin varchar(20),website varchar(20),dob varchar(20),ptype number,phno number,etype varchar(20),email_no varchar(20))")
root0=Tk()
root0.geometry("5000x5000")
Label(root0,text='Project Title: Phonebook',font='arial 20').grid(row=0,column=0)
Label(root0,text='Project of Python and Database',font='arial 20',fg='BLUE').grid(row=1,column=5)
Label(root0,text='Developed By: Divyansh Singh Sengar',font='arial 15',fg='red').grid(row=2,column=5)
Label(root0,text='---------------------------------------',font='arial 15').grid(row=3,column=5)
Label(root0,text='make mouse movement over screen to close',font='arial 15').grid(row=4,column=5)
def shut(e=1):
    root0.destroy()
root0.bind('<Motion>',shut)
root0.mainloop()
root=Tk()
a=PhotoImage(file='phonebook image.gif')
a=a.subsample(1,1)
Label(root,image=a).grid(row=0,column=2)
Label(root,text="First Name :",font="times 15 bold").grid(row=1,column=1)
fn=Entry(root)
fn.grid(row=1,column=3)

Label(root,text="Middle Name :",font="times 15 bold").grid(row=2,column=1)
mn=Entry(root)
mn.grid(row=2,column=3)

Label(root,text="Last Name :",font="times 15 bold").grid(row=3,column=1)
ln=Entry(root)
ln.grid(row=3,column=3)

Label(root,text="Company Name :",font="times 15 bold").grid(row=4,column=1)
cn=Entry(root)
cn.grid(row=4,column=3)

Label(root,text="Address :",font="times 15 bold").grid(row=5,column=1)
add=Entry(root)
add.grid(row=5,column=3)

Label(root,text="City :",font="times 15 bold").grid(row=6,column=1)
ct=Entry(root)
ct.grid(row=6,column=3)

Label(root,text="Pin Code :",font="times 15 bold").grid(row=7,column=1)
pc=Entry(root)
pc.grid(row=7,column=3)

Label(root,text="Website URL :",font="times 15 bold").grid(row=8,column=1)
ws=Entry(root)
ws.grid(row=8,column=3)

Label(root,text="Date Of Birth :",font="times 15 bold").grid(row=9,column=1)
dob=Entry(root)
dob.grid(row=9,column=3)

v1=StringVar()
Label(root,text="Select Phone type :",font="times 15 bold").grid(row=10,column=1)
Radiobutton(root,text="Office",variable=v1,value='office',tristatevalue="x").grid(row=10,column=2)
Radiobutton(root,text="Home",variable=v1,value='home',tristatevalue="x").grid(row=10,column=3)
Radiobutton(root,text="Mobile",variable=v1,value='mobile',tristatevalue="x").grid(row=10,column=4)
Label(root,text="Phone Number :").grid(row=11,column=1)
pn=Entry(root)
pn.grid(row=11,column=2)
Button(root,text="+").grid(row=11,column=3)

v2=StringVar()
Label(root,text="Select Email type :",font="times 15 bold").grid(row=12,column=1)
Radiobutton(root,text="Office",variable=v2,value='office',tristatevalue="x").grid(row=12,column=2)
Radiobutton(root,text="Home",variable=v2,value='home',tristatevalue="x").grid(row=12,column=3)
Label(root,text="Email id :").grid(row=13,column=1)
em=Entry(root)
em.grid(row=13,column=2)
Button(root,text="+").grid(row=13,column=3)
off='office'
hm='home'
mob='mobile'
v1.set("mobile")
v2.set("home")
def check(email):
    if(re.search(regex,email)):
        return 1
    else:
        return 0
def save():
    if (fn.get()=='' and mn.get()=='' and ln.get()=='' and cn.get()=='' and add.get()=='' and ct.get()=='' and pc.get()=='' and ws.get()=='' and dob.get()=='' and pn.get()=='' and em.get()==''):
        def fun():
            showerror('error','Enter atleast one field')
        fun()
    if((fn.get()==mn.get()==ln.get()) and (fn.get()==mn.get()==ln.get()!='')):
        def fun():
            showerror('error','Firstname,Middlename and Lastname should not be same')
        fun()
    if(len(pn.get())>14):
        def fun():
            showerror('error','digits length exceeded')
        fun()
    if(check(em.get())==0):
        def fun():
            showerror('error','Not a valid email id')
        fun()
    else:
        if v1.get()=='office' and v2.get()=='office':
            cur.execute("insert into contact (fn,mn,ln,company,address,city,pin,website,dob,ptype,phno,etype,email_no) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(fn.get(),mn.get(),ln.get(),cn.get(),add.get(),ct.get(),pc.get(),ws.get(),dob.get(),off,pn.get(),off,em.get()))
        if v1.get()=='office' and v2.get()=='home':
            cur.execute("insert into contact (fn,mn,ln,company,address,city,pin,website,dob,ptype,phno,etype,email_no) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(fn.get(),mn.get(),ln.get(),cn.get(),add.get(),ct.get(),pc.get(),ws.get(),dob.get(),off,pn.get(),hm,em.get()))
        if v1.get()=='home' and v2.get()=='office':
            cur.execute("insert into contact (fn,mn,ln,company,address,city,pin,website,dob,ptype,phno,etype,email_no) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(fn.get(),mn.get(),ln.get(),cn.get(),add.get(),ct.get(),pc.get(),ws.get(),dob.get(),hm,pn.get(),off,em.get()))
        if v1.get()=='home' and v2.get()=='home':
            cur.execute("insert into contact (fn,mn,ln,company,address,city,pin,website,dob,ptype,phno,etype,email_no) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(fn.get(),mn.get(),ln.get(),cn.get(),add.get(),ct.get(),pc.get(),ws.get(),dob.get(),hm,pn.get(),hm,em.get()))
        if v1.get()=='mobile' and v2.get()=='office':
            cur.execute("insert into contact (fn,mn,ln,company,address,city,pin,website,dob,ptype,phno,etype,email_no) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(fn.get(),mn.get(),ln.get(),cn.get(),add.get(),ct.get(),pc.get(),ws.get(),dob.get(),mob,pn.get(),off,em.get()))
        if v1.get()=='mobile' and v2.get()=='home':
            cur.execute("insert into contact (fn,mn,ln,company,address,city,pin,website,dob,ptype,phno,etype,email_no) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(fn.get(),mn.get(),ln.get(),cn.get(),add.get(),ct.get(),pc.get(),ws.get(),dob.get(),mob,pn.get(),hm,em.get()))
        cur.execute("select * from contact")
        root2=Tk()
        root2.geometry("600x600")
        Label(root2,text="First Name :",font="times 15 bold").grid(row=0,column=1)
        Label(root2,text=fn.get()).grid(row=0,column=3)

        Label(root2,text="Middle Name :",font="times 15 bold").grid(row=1,column=1)
        Label(root2,text=mn.get()).grid(row=1,column=3)
    
        Label(root2,text="Last Name :",font="times 15 bold").grid(row=2,column=1)
        Label(root2,text=ln.get()).grid(row=2,column=3)

        Label(root2,text="Company Name :",font="times 15 bold").grid(row=3,column=1)
        Label(root2,text=cn.get()).grid(row=3,column=3)

        Label(root2,text="Address :",font="times 15 bold").grid(row=4,column=1)
        Label(root2,text=add.get()).grid(row=4,column=3)

        Label(root2,text="City :",font="times 15 bold").grid(row=5,column=1)
        Label(root2,text=ct.get()).grid(row=5,column=3)

        Label(root2,text="Pin Code :",font="times 15 bold").grid(row=6,column=1)
        Label(root2,text=pc.get()).grid(row=6,column=3)
    
        Label(root2,text="Website URL :",font="times 15 bold").grid(row=7,column=1)
        Label(root2,text=ws.get()).grid(row=7,column=3)

        Label(root2,text="Date Of Birth :",font="times 15 bold").grid(row=8,column=1)
        Label(root2,text=dob.get()).grid(row=8,column=3)

        Label(root2,text="Phone type :",font="times 15 bold").grid(row=9,column=1)
        Label(root2,text=v1.get()).grid(row=9,column=3)

        Label(root2,text="Phone Number :",font="times 15 bold").grid(row=10,column=1)
        Label(root2,text=pn.get()).grid(row=10,column=3)

        Label(root2,text="Email type :",font="times 15 bold").grid(row=11,column=1)
        Label(root2,text=v2.get()).grid(row=11,column=3)
    
        Label(root2,text="Email Id :",font="times 15 bold").grid(row=12,column=1)
        Label(root2,text=em.get()).grid(row=12,column=3)

        Label(root2,text="CONTACT SAVED!",font="times 15 bold").grid(row=13,column=2)

        fn.delete(0,END)
        mn.delete(0,END)
        ln.delete(0,END)
        cn.delete(0,END)
        add.delete(0,END)
        ct.delete(0,END)
        pc.delete(0,END)
        ws.delete(0,END)
        dob.delete(0,END)
        fn.delete(0,END)
        pn.delete(0,END)
        em.delete(0,END)
        v1.set("mobile")
        v2.set("home")
        def close2(x):
            root2.destroy()
        root2.bind("<Key>",close2)
        Label(root2,text="press any key to continue...",font="times 15 bold").grid(row=14,column=2)
        root2.mainloop()
def search():
    root3=Tk()
    root3.geometry("600x600")
    Label(root3,text="Search Box  ",font="times 20 bold").grid(row=0,column=0)
    sb=Entry(root3)
    sb.grid(row=0,column=1)
    def submit(x):
        lb=Listbox(root3,height=50)
        lb.grid(row=1,column=0)
        i=0
        j=0
        cur.execute("select fn" + " from contact where fn like (?) order by fn",('%'+sb.get()+'%',))
        record=cur.fetchall()
        while(i!=len(record)):
            j=0
            while(j!=len(record[i])):
                lb.insert(END,record[i][j])
                j=j+1
            i=i+1
        def get_list(x):
            index=lb.curselection()
            text=lb.get(index)
            cur.execute("select id from contact where fn=(?)",(text,))
            id_no=cur.fetchall()
            try:
                if len(id_no)>1:
                    cur.execute("select * from contact where fn=(?) and id=(?) order by id",(text,id_no[index[0]][0]))
                elif len(id_no)==1:
                    cur.execute("select * from contact where fn=(?) order by id",(text,))
            except IndexError:
                cur.execute("select * from contact where fn=(?) order by id",(text,))
            record=cur.fetchall()
            root4=Tk()
            root4.geometry("600x600")
            Label(root4,text="FIRST NAME: ").grid(row=0,column=0)
            Label(root4,text=record[0][1]).grid(row=0,column=1)
            Label(root4,text="MIDDLE NAME: ").grid(row=1,column=0)
            Label(root4,text=record[0][2]).grid(row=1,column=1)
            Label(root4,text="LAST NAME").grid(row=2,column=0)
            Label(root4,text=record[0][3]).grid(row=2,column=1)
            Label(root4,text="COMPANY NAME").grid(row=3,column=0)
            Label(root4,text=record[0][4]).grid(row=3,column=1)
            Label(root4,text="ADDRESS").grid(row=4,column=0)
            Label(root4,text=record[0][5]).grid(row=4,column=1)
            Label(root4,text="CITY").grid(row=5,column=0)
            Label(root4,text=record[0][6]).grid(row=5,column=1)
            Label(root4,text="PIN").grid(row=6,column=0)
            Label(root4,text=record[0][7]).grid(row=6,column=1)
            Label(root4,text="WEBSITE URL").grid(row=7,column=0)
            Label(root4,text=record[0][8]).grid(row=7,column=1)
            Label(root4,text="DOB").grid(row=8,column=0)
            Label(root4,text=record[0][9]).grid(row=8,column=1)
            Label(root4,text="PHONETYPE").grid(row=9,column=0)
            Label(root4,text=record[0][10]).grid(row=9,column=1)
            Label(root4,text="PHONE NUMBER").grid(row=10,column=0)
            Label(root4,text=record[0][11]).grid(row=10,column=1)
            Label(root4,text="EMAILTYPE").grid(row=11,column=0)
            Label(root4,text=record[0][12]).grid(row=11,column=1)
            Label(root4,text="EMAIL ID").grid(row=12,column=0)
            Label(root4,text=record[0][13]).grid(row=12,column=1)
            def edit():
                new_fname=Entry(root4)
                new_fname.grid(row=0,column=2)
                new_mname=Entry(root4)
                new_mname.grid(row=1,column=2)
                new_lname=Entry(root4)
                new_lname.grid(row=2,column=2)
                new_cname=Entry(root4)
                new_cname.grid(row=3,column=2)
                new_add=Entry(root4)
                new_add.grid(row=4,column=2)
                new_city=Entry(root4)
                new_city.grid(row=5,column=2)
                new_pin=Entry(root4)
                new_pin.grid(row=6,column=2)
                new_website=Entry(root4)
                new_website.grid(row=7,column=2)
                new_dob=Entry(root4)
                new_dob.grid(row=8,column=2)
                new_ptype=Entry(root4)
                new_ptype.grid(row=9,column=2)
                new_pnumber=Entry(root4)
                new_pnumber.grid(row=10,column=2)
                new_etype=Entry(root4)
                new_etype.grid(row=11,column=2)
                new_email=Entry(root4)
                new_email.grid(row=12,column=2)
                def new_f():
                    cur.execute("update contact set fn=(?) where id=(?)",(new_fname.get(),record[0][0]))
                    new_fname.delete(0,END)
                def new_m():
                    cur.execute("update contact set mn=(?) where id=(?)",(new_mname.get(),record[0][0]))
                    new_mname.delete(0,END)
                def new_l():
                    cur.execute("update contact set ln=(?) where id=(?)",(new_lname.get(),record[0][0]))
                    new_lname.delete(0,END)
                def new_c():
                    cur.execute("update contact set company=(?) where id=(?)",(new_cname.get(),record[0][0]))
                    new_cname.delete(0,END)
                def new_a():
                    cur.execute("update contact set address=(?) where id=(?)",(new_add.get(),record[0][0]))
                    new_add.delete(0,END)
                def new_ct():
                    cur.execute("update contact set city=(?) where id=(?)",(new_city.get(),record[0][0]))
                    new_city.delete(0,END)
                def new_p():
                    cur.execute("update contact set pin=(?) where id=(?)",(new_pin.get(),record[0][0]))
                    new_pin.delete(0,END)
                def new_w():
                    cur.execute("update contact set website=(?) where id=(?)",(new_website.get(),record[0][0]))
                    new_website.delete(0,END)
                def new_d():
                    cur.execute("update contact set dob=(?) where id=(?)",(new_dob.get(),record[0][0]))
                    new_dob.delete(0,END)
                def new_pt():
                    cur.execute("update contact set ptype=(?) where id=(?)",(new_ptype.get(),record[0][0]))
                    new_ptype.delete(0,END)
                def new_pnum():
                    cur.execute("update contact set phno=(?) where id=(?)",(new_pnumber.get(),record[0][0]))
                    new_pnumber.delete(0,END)
                def new_et():
                    cur.execute("update contact set etype=(?) where id=(?)",(new_etype.get(),record[0][0]))
                    new_etype.delete(0,END)
                def new_em():
                    cur.execute("update contact set email_no=(?) where id=(?)",(new_email.get(),record[0][0]))
                    new_email.delete(0,END)
                Button(root4,text='EDIT',command=new_f).grid(row=0,column=3)
                Button(root4,text='EDIT',command=new_m).grid(row=1,column=3)
                Button(root4,text='EDIT',command=new_l).grid(row=2,column=3)
                Button(root4,text='EDIT',command=new_c).grid(row=3,column=3)
                Button(root4,text='EDIT',command=new_a).grid(row=4,column=3)
                Button(root4,text='EDIT',command=new_ct).grid(row=5,column=3)
                Button(root4,text='EDIT',command=new_p).grid(row=6,column=3)
                Button(root4,text='EDIT',command=new_w).grid(row=7,column=3)
                Button(root4,text='EDIT',command=new_d).grid(row=8,column=3)
                Button(root4,text='EDIT',command=new_pt).grid(row=9,column=3)
                Button(root4,text='EDIT',command=new_pnum).grid(row=10,column=3)
                Button(root4,text='EDIT',command=new_et).grid(row=11,column=3)
                Button(root4,text='EDIT',command=new_em).grid(row=12,column=3)
            Button(root4,text='EDIT',command=edit).grid(row=13,column=0)
            Button(root4,text='CLOSE',command=root4.destroy).grid(row=14,column=1)
            root4.mainloop()
        lb.bind("<<ListboxSelect>>",get_list)
        def delete_contact():
            index=lb.curselection()
            text=lb.get(index)
            cur.execute("select * from contact where fn=(?)",(text,))
            record=cur.fetchall()
            cur.execute("delete from contact where fn=(?) and id=(?)",(text,record[0][0]))
            lb.delete(index)
        Button(root3,text="delete",command=delete_contact).grid(row=0,column=3)
    root3.bind("<Key>",submit)
    Button(root3,text="CLOSE",command=root3.destroy).grid(row=0,column=4)
    root3.mainloop()
Button(root,text="SAVE",font="times 15 bold",command=save).grid(row=15,column=1)
Button(root,text="SEARCH",font="times 15 bold",command=search).grid(row=15,column=2)
Button(root,text="CLOSE",font="times 15 bold",command=root.destroy).grid(row=15,column=3)
root.geometry("800x800")
root.mainloop()
con.commit()
