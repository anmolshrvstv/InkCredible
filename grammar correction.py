import language_tool_python
tool = language_tool_python.LanguageTool("en-US")
corrected_text = tool.correct(text)
print("Corrected Text:", corrected_text)
