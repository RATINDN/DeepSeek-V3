async function generateText() {
  const prompt = document.getElementById('prompt').value;
  const response = await fetch('http://localhost:5000/generate', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ prompt: prompt, max_new_tokens: 100, temperature: 1.0 })
  });
  const data = await response.json();
  document.getElementById('result').innerText = data.completion;
}