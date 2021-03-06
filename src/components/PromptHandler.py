import click


class PromptHandler:
    def create_text_prompt(self, text, validator=False):
        prompt_value = click.prompt(text)

        if not validator:
            return prompt_value

        prompt_value = self.validate_prompt(text, prompt_value, validator)
        return prompt_value

    def validate_prompt(self, text, prompt_value, validator):
        valid_prompt = validator(prompt_value)

        while not valid_prompt:
            prompt_value = click.prompt(text)
            valid_prompt = validator(prompt_value)

        return prompt_value
