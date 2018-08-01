from yaml import load
from jinja2 import Template

my_variables_file=open('variables.yml', 'r')
my_variables_in_string=my_variables_file.read()
my_variables_in_yaml=load(my_variables_in_string)
my_variables_file.close()

f=open('minion.j2')
my_template = Template(f.read())
f.close()

f=open('minion/minion','w')
f.write(my_template.render(my_variables_in_yaml))
f.close()

f=open('proxy.j2')
my_template = Template(f.read())
f.close()

f=open('minion/proxy','w')
f.write(my_template.render(my_variables_in_yaml))
f.close()

f=open('master/proxy','w')
f.write(my_template.render(my_variables_in_yaml))
f.close()

f=open('syslog.j2')
my_template = Template(f.read())
f.close()

f=open('master/salt/syslog.conf','w')
f.write(my_template.render(my_variables_in_yaml))
f.close()

f=open('pillars_top.j2')
my_template = Template(f.read())
f.close()

f=open('master/pillar/top.sls','w')
f.write(my_template.render(my_variables_in_yaml))
f.close()

f=open('pillars_device.j2')
my_template = Template(f.read())
f.close()

for item in my_variables_in_yaml['junos']:
    f=open('master/pillar/' + item['name'] +'-details.sls','w')
    f.write(my_template.render(item))
    f.close()


