workflow "Test on push" {
  on = "push"
  resolves = [
    "Check Python style",
    "Python test latest",
  ]
}

action "Check Python style" {
  uses = "bulv1ne/python-style-check@master"
}

action "Python test latest" {
  uses = "docker://python:latest"
  runs = "python setup.py test"
}
