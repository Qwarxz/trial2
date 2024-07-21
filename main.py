import yaml

# Step 1: Read the .tex file
with open('lctrncs.tex', 'r') as file:
    tex_content = file.read()


with open('config.yaml', 'r') as file:
    conf = yaml.safe_load(file)
# Step 2: Manipulate the string
tex_content = tex_content.replace('[company]', conf['company'])
tex_content = tex_content.replace('[co]', conf['co'])
tex_content = tex_content.replace(('[position]'), conf['position'])
tex_content = tex_content.replace('<university1>', conf['university1'])
tex_content = tex_content.replace('<university2>', conf['university2'])
tex_content = tex_content.replace('<programme>', conf['programme'])
tex_content = tex_content.replace('<Hiring Staff>', conf['Hiring Staff'])
tex_content = tex_content.replace('[Hiring Manager\'s Name]',
                                  conf['Hiring Manager\'s Name'])
tex_content = tex_content.replace('[company address]', conf['company address'])
tex_content = tex_content.replace('[City, State, Zip Code]',
                                  conf['City, State, Zip Code'])
tex_content = tex_content.replace('[specific reason related to the company or position, e.g., innovative projects, company culture, industry leadership]', conf['reason'])
# Step 3: Write back to the .tex file
with open('example.tex', 'w') as file:
    file.write(tex_content)
