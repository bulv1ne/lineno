workflow "Test on push" {
  on = "push"
  resolves = [
    "Check Python style",
    "Python test latest",
    "Python test 2.7",
    "Python test 3.5",
    "Python test 3.6",
    "Python test 3.7",
  ]
}

action "Check Python style" {
  uses = "bulv1ne/python-style-check@master"
}

action "Python test latest" {
  uses = "docker://python:latest"
  runs = "python setup.py test"
}

action "Python test 2.7" {
  uses = "docker://python:2.7"
  runs = "python setup.py test"
}

action "Python test 3.5" {
  uses = "docker://python:3.5"
  runs = "python setup.py test"
}

action "Python test 3.6" {
  uses = "docker://python:3.6"
  runs = "python setup.py test"
}

action "Python test 3.7" {
  uses = "docker://python:3.7"
  runs = "python setup.py test"
}
