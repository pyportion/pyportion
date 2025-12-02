from dataclasses import dataclass


@dataclass
class Config:
    portion_dir = "pyportion"
    portion_file = '.pyportion.yml'
    github_base_url = "https://github.com"
    gitlab_base_url = "https://gitlab.com"
