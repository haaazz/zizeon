<template>
    <div class="content">
      <h1>적금</h1>
      <table>
        <thead>
          <tr>
            <th>번호</th>
            <th>상품명</th>
            <th>회사명</th>
            <th>공시월</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="saving in paginatedSavings" :key="saving.id">
            <td>{{ saving.id }}</td>
            <td>{{ saving.fin_prdt_nm }}</td>
            <td>{{ saving.kor_co_nm }}</td>
            <td>{{ saving.dcls_month }}</td>
          </tr>
        </tbody>
      </table>
      <div class="pagination">
        <button @click="prevPage" :disabled="currentPage === 1"> 이전 </button>
        <span>{{ currentPage }} / {{ totalPages }}</span>
        <button @click="nextPage" :disabled="currentPage === totalPages">다음</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue'
  import { useSavingStore } from '@/stores/saving'
  
  const store = useSavingStore()
  const savings = ref([])
  const currentPage = ref(1)
  const itemsPerPage = 15

  const totalPages = computed(() => {
    return Math.ceil(savings.value.length / itemsPerPage)
  })

  const paginatedSavings = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage
    const end = start + itemsPerPage
    return savings.value.slice(start, end)
  })

  const nextPage = () => {
    if (currentPage.value < totalPages.value) {
      currentPage.value++
    }
  }
  
  const prevPage = () => {
    if (currentPage.value > 1) {
      currentPage.value--
    }
  }
  
  onMounted(async () => {
    await store.getSaving()
    savings.value = store.savings
  })
  </script>
  
  <style scoped>
  .content {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  table {
    width: 80%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }
  
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
  }
  
  th {
    background-color: #f2f2f2;
  }
  
  .pagination {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  
  button {
    padding: 5px 10px;
    cursor: pointer;
  }
  
  button:disabled {
    cursor: not-allowed;
    opacity: 0.5;
  }
  </style>
  