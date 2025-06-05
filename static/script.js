async function loadProducts() {
  const res = await fetch("/api/products");
  const products = await res.json();
  const container = document.getElementById("products");
  container.innerHTML = '';
  products.forEach(p => {
    container.innerHTML += `
      <div class="product-card">
        <img src="${p.image}" alt="${p.name}">
        <h3>${p.name}</h3>
        <p>${p.price} ريال</p>
      </div>
    `;
  });
}

window.onload = loadProducts;
