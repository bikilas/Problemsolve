class Solution:
    def interpret(self, command: str) -> str:
        interpreted = command.replace("()", "o").replace("(al)", "al")
        return interpreted
