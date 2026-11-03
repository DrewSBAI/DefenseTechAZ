const search = document.querySelector('#search');
const city = document.querySelector('#city');
const rows = [...document.querySelectorAll('tbody tr')];
const searchable = rows.map(row => ({ row, text: row.textContent.toLocaleLowerCase() }));
function filter() {
  const query = search.value.trim().toLocaleLowerCase();
  let count = 0;
  for (const { row, text } of searchable) {
    row.hidden = !(text.includes(query) && (!city.value || row.dataset.city === city.value));
    if (!row.hidden) count++;
  }
  document.querySelector('#results').textContent = `${count} of ${rows.length} companies`;
  document.querySelector('#empty').hidden = count !== 0;
}
document.querySelector('.filters').hidden = false;
search.addEventListener('input', filter);
city.addEventListener('change', filter);
document.querySelector('#reset').addEventListener('click', () => {
  search.value = '';
  city.value = '';
  filter();
  search.focus();
});
