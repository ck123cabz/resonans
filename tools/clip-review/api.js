// GET when there is no body, POST JSON when there is; throws on any non-2xx.
export async function api(path, body) {
  const res = await fetch(path, body && {
    method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error(`${path}: ${res.status}`);
  return res.json();
}
