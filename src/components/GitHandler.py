import re
import os
from git import Repo

class GitHandler:
  def __init__(self,repo_name: str, repo_url:str, repo_directory: str) -> None:
      self.repo_url = repo_url
      self.repo_directory = repo_directory
      self.repo_name = repo_name

  def filter_repo_name(self):
    filtered_name = re.sub('[^A-Za-z0-9]+', '', self.repo_name)
    return filtered_name.lower()

  def clone_repo(self):
    filtered_repo_name = self.filter_repo_name()
    clone_to_dir = os.path.join(self.repo_directory, filtered_repo_name)

    Repo.clone_from(self.repo_url, clone_to_dir)

    return clone_to_dir
