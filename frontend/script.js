async function analyzeIncident() {
  const service = document.getElementById("service").value;
  const error = document.getElementById("error").value;

  if (!service || !error) {
    alert("Fill all fields");
    return;
  }

  document.getElementById("analyzeBtn").disabled = true;
  document.getElementById("loader").classList.remove("hidden");
  document.getElementById("result").classList.add("hidden");

  const res = await fetch("http://127.0.0.1:8000/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ service, error })
  });

  const data = await res.json();

  document.getElementById("severity").innerText = data.severity;
  document.getElementById("cause").innerText = data.root_cause;
  document.getElementById("solution").innerText = data.solution;
  document.getElementById("confidence").innerText = data.confidence + "%";

  document.getElementById("loader").classList.add("hidden");
  document.getElementById("result").classList.remove("hidden");
  document.getElementById("analyzeBtn").disabled = false;
}
