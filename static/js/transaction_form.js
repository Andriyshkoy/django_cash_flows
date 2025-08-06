(function () {
  function ready(fn) {
    if (document.readyState !== 'loading') {
      fn();
    } else {
      document.addEventListener('DOMContentLoaded', fn);
    }
  }

  ready(function () {
    const txTypeSelect = document.getElementById('id_tx_type');
    const categorySelect = document.getElementById('id_category');
    const subCategorySelect = document.getElementById('id_sub_category');

    function disable(select, state) {
      if (select) {
        select.disabled = state;
      }
    }

    function reset(select) {
      if (select) {
        select.innerHTML = '<option value="">---------</option>';
      }
    }

    function populate(select, items, selected) {
      if (!select) return;
      reset(select);
      items.forEach(function (item) {
        const option = document.createElement('option');
        option.value = item.id;
        option.textContent = item.name;
        if (selected && String(selected) === String(item.id)) {
          option.selected = true;
        }
        select.appendChild(option);
      });
    }

    function fetchCategories(txTypeId, selected) {
      disable(categorySelect, true);
      disable(subCategorySelect, true);
      reset(categorySelect);
      reset(subCategorySelect);
      if (!txTypeId) return;
      fetch(`/api/categories/?tx_type=${txTypeId}`)
        .then((resp) => resp.json())
        .then((data) => {
          const items = data.results || data;
          populate(categorySelect, items, selected);
          disable(categorySelect, false);
        });
    }

    function fetchSubCategories(categoryId, selected) {
      disable(subCategorySelect, true);
      reset(subCategorySelect);
      if (!categoryId) return;
      fetch(`/api/sub-categories/?category=${categoryId}`)
        .then((resp) => resp.json())
        .then((data) => {
          const items = data.results || data;
          populate(subCategorySelect, items, selected);
          disable(subCategorySelect, false);
        });
    }

    txTypeSelect &&
      txTypeSelect.addEventListener('change', function (e) {
        fetchCategories(e.target.value);
      });

    categorySelect &&
      categorySelect.addEventListener('change', function (e) {
        fetchSubCategories(e.target.value);
      });

    if (txTypeSelect && txTypeSelect.value) {
      const currentCategory = categorySelect && categorySelect.value;
      const currentSubCategory = subCategorySelect && subCategorySelect.value;
      fetchCategories(txTypeSelect.value, currentCategory);
      if (currentCategory) {
        fetchSubCategories(currentCategory, currentSubCategory);
      }
    }
  });
})();