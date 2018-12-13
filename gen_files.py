#!/usr/bin/env python3
import yaml
import os

def gen_main_readme(conf):
    f = open('README.md', 'w')
    f.write("# Reversing Challenges List\n")
    
    criterions = conf['criterions']
    problems = conf['problems']
    for c in criterions:
        f.write("## " + c + "\n")
        if problems[c] is None:
            continue
        for p in problems[c]:
            ctf_name = p['ctf_name']
            problem_name = str(p['problem_name'])
            f.write(' * [{0:s} : {1:s}]({2:s}/{3:s}/README.md)\n'.format(ctf_name, problem_name, c.replace(' ', '_'), ctf_name.replace(' ', '_') + '_' + problem_name.replace(' ', '_')))
        f.write('\n')

    f.close()

def gen_problem_dirs(conf):
    criterions = conf['criterions']
    problems = conf['problems']
    for c in criterions:
        if problems[c] is None:
            continue
        for p in problems[c]:
            ctf_name = p['ctf_name']
            problem_name = str(p['problem_name'])
            try:
                os.makedirs('{0:s}/{1:s}'.format(c.replace(' ', '_'), ctf_name.replace(' ', '_') + '_' + problem_name.replace(' ', '_')))
            except FileExistsError:
                pass

def gen_readme(readme_path, ctf_name, problem_name, points, solves, description):
    d = open('problem_template.md', 'r').read()
    d = d.replace('CTF_NAME', ctf_name)
    d = d.replace('PROBLEM_NAME', problem_name)
    d = d.replace('POINTS', points)
    d = d.replace('SOLVES', solves)
    d = d.replace('DESCRIPTION', description)
    d = d.replace('ATTACHMENT', problem_name.replace(' ', '_'))
    open(readme_path, 'w').write(d)


def gen_writeup(writeup_path, ctf_name, problem_name, flag):
    d = open('writeup_template.md', 'r').read()
    d = d.replace('CTF_NAME', ctf_name)
    d = d.replace('PROBLEM_NAME', problem_name)
    d = d.replace('FLAG', flag)
    open(writeup_path, 'w').write(d)

def gen_problem_files(conf):
    criterions = conf['criterions']
    problems = conf['problems']
    for c in criterions:
        if problems[c] is None:
            continue
        for p in problems[c]:
            ctf_name = p['ctf_name']
            problem_name = str(p['problem_name'])
            points = p['points']
            solves = p['solves']
            description = p['description']
            flag = p['flag']

            path = '{0:s}/{1:s}/'.format(c.replace(' ', '_'), ctf_name.replace(' ', '_') + '_' + problem_name.replace(' ', '_'))
            readme_path = path + 'README.md'
            writeup_path = path + 'writeup.md'
            if os.path.exists(readme_path):
                continue
            gen_readme(readme_path, ctf_name, problem_name, str(points), str(solves), description.strip())
            gen_writeup(writeup_path, ctf_name, problem_name, flag)
            
def main():
    conf = yaml.load(open('problem.yaml', 'rb').read())
    gen_main_readme(conf)
    gen_problem_dirs(conf)
    gen_problem_files(conf)

if __name__ == '__main__':
    main()
