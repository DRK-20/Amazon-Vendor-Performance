def parse_genai_response(response_text):
    try:
        lines = response_text.strip().split("\n")
        issues_index = lines.index('Issues:') + 1
        suggestions_index = lines.index('Suggestions:') + 1

        issues = []
        suggestions = []

        for line in lines[issues_index:]:
            if line.startswith('Suggestions:'):
                break

            if line.strip():
                data = line.strip()
               
                if data[1] == '.':
                    issues.append(data[3:])  # Skip "1. "

        for line in lines[suggestions_index:]:
            if line.strip():
                data = line.strip()

                if data[1] == '.':
                    suggestions.append(data[3:])

        print(issues)
        print(suggestions)

        return {'issues': issues, 'suggestions': suggestions}
    
    except Exception as e:
        print(f'Error parsing GenAI response: {e}')
        return {'issues': [], 'suggestions': []}
