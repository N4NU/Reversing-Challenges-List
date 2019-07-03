#!/usr/bin/env python3
import yaml
import os

def escape_path(s):
    return s.replace(' ', '_').replace('/', '_')

def gen_main_readme(conf):
    f = open('README.md', 'w')

    f.write("# Reversing Challenges List\n\n")
    msg = ''
    msg += 'If there is no writeup about reversing tasks of past CTF and you need, please make the issue.\n\n'
    msg += '過去のCTFのrev問でwriteupが無かったり，日本語のwriteupがほしい場合にissueを立ててくれれば出来るだけ解いて日本語のwriteupを書いていこうと思います．\n\n'
    f.write(msg)
    
    criterions = conf['criterions']
    for criterion in criterions:
        problems = yaml.load(open('./problem_list/' + escape_path(criterion) + '.yaml', 'r').read())
        f.write("## " + criterion + "\n")
        for p in problems:
            ctf_name = p['ctf_name']
            problem_name = str(p['problem_name'])
            f.write(' * [{0:s} : {1:s}]({2:s}/{3:s}/README.md)\n'.format(ctf_name, problem_name, escape_path(criterion), escape_path(ctf_name) + '_' + escape_path(problem_name)))
        f.write('\n')

    f.close()

def gen_problem_dirs(conf):
    criterions = conf['criterions']
    for criterion in criterions:
        problems = yaml.load(open('./problem_list/' + escape_path(criterion) + '.yaml', 'r').read())
        for p in problems:
            ctf_name = p['ctf_name']
            problem_name = str(p['problem_name'])
            try:
                os.makedirs('{0:s}/{1:s}'.format(escape_path(criterion), escape_path(ctf_name) + '_' + escape_path(problem_name)))
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
    for criterion in criterions:
        problems = yaml.load(open('./problem_list/' + escape_path(criterion) + '.yaml', 'r').read())
        for p in problems:
            ctf_name = p['ctf_name']
            problem_name = str(p['problem_name'])
            points = p['points']
            solves = p['solves']
            description = p['description']
            flag = str(p['flag'])

            path = '{0:s}/{1:s}/'.format(escape_path(criterion), escape_path(ctf_name) + '_' + escape_path(problem_name))
            readme_path = path + 'README.md'
            writeup_path = path + 'writeup.md'
            if os.path.exists(readme_path):
                continue
            gen_readme(readme_path, ctf_name, problem_name, str(points), str(solves), description.strip())
            gen_writeup(writeup_path, ctf_name, problem_name, flag)
            
def main():
    conf = yaml.load(open('conf.yaml', 'r').read())
    gen_main_readme(conf)
    gen_problem_dirs(conf)
    gen_problem_files(conf)

if __name__ == '__main__':
    main()
