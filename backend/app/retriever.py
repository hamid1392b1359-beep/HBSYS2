def simple_match(question: str, knowledge: dict):
    q = question.lower()
    matched_concepts = []
    matched_principles = []
    principle_ids = set()

    for concept in knowledge["concepts"]:
        names = [concept["name"]] + concept.get("aliases", [])
        if any(name.lower() in q for name in names):
            matched_concepts.append(concept)
            for pid in concept.get("related_principles", []):
                principle_ids.add(pid)

    for p in knowledge["principles"]:
        if p["id"] in principle_ids:
            matched_principles.append(p)

    if not matched_principles:
        matched_principles = knowledge["principles"][:5]

    return {
        "concepts": matched_concepts,
        "principles": matched_principles,
        "chapters": knowledge["chapters"][:3500]
    }
