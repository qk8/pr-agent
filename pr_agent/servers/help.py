# pyright: ignore[reportImplicitStringConcatenation]
from __future__ import annotations
class HelpMessage:
    @staticmethod
    def get_general_commands_text():
       commands_text = "> - **/review**: Request a review of your Pull Request.   \n" \
                "> - **/describe**: Update the PR title and description based on the contents of the PR.   \n" \
                "> - **/improve [--extended]**: Suggest code improvements. Extended mode provides a higher quality feedback.   \n" \
                "> - **/ask \\<QUESTION\\>**: Ask a question about the PR.   \n" \
                "> - **/update_changelog**: Update the changelog based on the PR's contents.   \n" \
                "> - **/help_docs \\<QUESTION\\>**: Given a path to documentation (either for this repository or for a given one), ask a question.   \n" \
                "> - **/add_docs**: Generate docstring for new components introduced in the PR.   \n" \
                "> - **/generate_labels**: Generate labels for the PR based on the PR's contents.   \n\n" \
                ">See the [tools guide](https://pr-agent-docs.codium.ai/tools/) for more details.\n" \
                ">To list the possible configuration parameters, add a **/config** comment.   \n"
       return commands_text


    @staticmethod
    def get_general_bot_help_text():
        output = f"> To invoke the PR-Agent, add a comment using one of the following commands:  \n{HelpMessage.get_general_commands_text()} \n"
        output += "> - **/reviewx**: Request a review of your Pull Request using the PR-Agent tool.\n"
        output += "> - **/describe**: Update the PR title and description with the tool output.\n"
        output += ">To list the possible configuration parameters, add a **/config** comment.\n"
        return output


    @staticmethod
    def get_pr_replica_commands_text():
        commands_text = "> - **/describe**: Update the PR title and description with the tool output.   \n" \
                "> - **/review**: Request a review of your Pull Request.   \n"
        return commands_text


    @staticmethod
    def get_pr_replica_bot_help_text():
        output = "> To invoke the PR-Agent, add a comment using one of the following commands:  \n" \
                "> - **/describe**: Update the PR title and description with the tool output.\n" \
                "> - **/review**: Request a review of your Pull Request.\n"
        return output
