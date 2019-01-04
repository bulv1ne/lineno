workflow "Test on push" {
  on = "push"
  resolves = ["Check Python style"]
}

action "Check Python style" {
  uses = "bulv1ne/python-style-check@master"
}
