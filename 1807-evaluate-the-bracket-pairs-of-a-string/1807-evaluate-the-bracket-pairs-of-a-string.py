class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        data = dict(knowledge)

        result = re.findall(r"\((.*?)\)", s)

        for key in result:
            if key in data:
                s = s.replace("(" + key + ")", data[key])
            else:
                s = s.replace("(" + key + ")", "?")

        return s