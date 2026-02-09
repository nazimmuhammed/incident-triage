def analyze_incident(incident: dict):
    service = incident.get("service", "Unknown service")
    error = incident.get("error", "No error message")
    severity = incident.get("severity", "low")

    confidence = "high"

    if "timeout" in error.lower():
        root_cause = "Possible database or network latency issue"
        action = "Check DB connections, increase timeout, review logs"

    elif "memory" in error.lower():
        root_cause = "Possible memory leak"
        action = "Inspect memory usage, restart service, analyze heap"

    else:
        # 👇 FALLBACK TO SECOND AI
        fallback = fallback_ai_analysis(incident)
        root_cause = fallback["root_cause"]
        action = fallback["recommended_action"]
        confidence = fallback["confidence"]

    return {
        "service": service,
        "detected_severity": severity,
        "root_cause": root_cause,
        "recommended_action": action,
        "analysis_confidence": confidence
    }
def fallback_ai_analysis(incident: dict):
    # Simulating another AI or external API
    return {
        "root_cause": "Potential misconfiguration or edge-case failure",
        "recommended_action": "Verify recent deployments, configs, and retry the operation",
        "confidence": "medium"
    }

 