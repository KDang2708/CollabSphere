import openai
from ..config import OPENAI_API_KEY, OPENAI_MODEL
from typing import List, Dict, Optional

class ChatGPTAIService:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        self.model = OPENAI_MODEL

    def brainstorm_ideas(self, topic: str, context: Optional[str] = None) -> List[str]:
        """
        Generate ideas for a given topic using ChatGPT.
        """
        prompt = f"Brainstorm ideas for: {topic}"
        if context:
            prompt += f"\nContext: {context}"
        prompt += "\nProvide a list of 5-10 creative ideas."

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        ideas = response.choices[0].message.content.strip().split('\n')
        return [idea.strip() for idea in ideas if idea.strip()]

    def project_guidance(self, project_description: str, current_stage: str) -> str:
        """
        Provide guidance for project development.
        """
        prompt = f"Project: {project_description}\nCurrent Stage: {current_stage}\nProvide detailed guidance on next steps, best practices, and potential challenges."

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()

    def suggest_solutions(self, problem: str, constraints: Optional[List[str]] = None) -> List[str]:
        """
        Suggest solutions for a given problem.
        """
        prompt = f"Problem: {problem}"
        if constraints:
            prompt += f"\nConstraints: {', '.join(constraints)}"
        prompt += "\nSuggest 3-5 practical solutions."

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=600,
            temperature=0.6
        )
        solutions = response.choices[0].message.content.strip().split('\n')
        return [solution.strip() for solution in solutions if solution.strip()]

    def generate_project_info(self, project_name: str, objectives: List[str], milestones: List[str]) -> Dict[str, str]:
        """
        Automatically generate project information.
        """
        prompt = f"Generate detailed project information for:\nName: {project_name}\nObjectives: {', '.join(objectives)}\nMilestones: {', '.join(milestones)}\nProvide: Description, Timeline, Resources needed, Risks."

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800,
            temperature=0.4
        )
        content = response.choices[0].message.content.strip()
        # Parse the response into a dictionary (simplified parsing)
        sections = content.split('\n\n')
        info = {}
        for section in sections:
            if ':' in section:
                key, value = section.split(':', 1)
                info[key.strip()] = value.strip()
        return info

    def analyze_progress(self, progress_data: Dict[str, any]) -> str:
        """
        Analyze team progress and provide advice.
        """
        prompt = f"Analyze the following project progress data and provide advice:\n{progress_data}\nFocus on bottlenecks, improvements, and next priorities."

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=700,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()

    def analyze_contributions(self, contributions_data: List[Dict[str, any]]) -> str:
        """
        Analyze individual contributions and provide feedback.
        """
        prompt = f"Analyze the following team member contributions and provide feedback:\n{contributions_data}\nHighlight strengths, areas for improvement, and suggestions."

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=700,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()

    def chatbot_response(self, user_message: str, conversation_history: Optional[List[Dict[str, str]]] = None) -> str:
        """
        Generate a chatbot response.
        """
        messages = conversation_history or []
        messages.append({"role": "user", "content": user_message})

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
