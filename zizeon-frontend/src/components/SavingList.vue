<template>
    <div class="content">
      <h1>적금</h1>
      <table>
        <thead>
          <tr>
            <th>번호</th>
            <th>상품명</th>
            <th>회사명</th>
            <th>적립유형명</th>
            <th>6개월</th>
            <th>12개월</th>
            <th>24개월</th>
            <th>36개월</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="saving in paginatedSavings" :key="saving.id">
            <td>{{ saving.id }}</td>
            <td><RouterLink :to="{ name: 'SavingDetail', params: { id: saving.id } }">{{ saving.fin_prdt_nm }}</RouterLink></td>
            <td>{{ saving.kor_co_nm }}</td>
            <td>자유적립식</td>
            <td v-for="option in changeOption(saving, '자유적립식', 6)"><p>{{ option.intr_rate }}</p></td>
            <td v-for="option in changeOption(saving, '자유적립식', 12)"><p>{{ option.intr_rate }}</p></td>
            <td v-for="option in changeOption(saving, '자유적립식', 24)"><p>{{ option.intr_rate }}</p></td>
            <td v-for="option in changeOption(saving, '자유적립식', 36)"><p>{{ option.intr_rate }}</p></td>
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
  import { RouterLink } from 'vue-router'
  
  const store = useSavingStore()
  const savings = ref([])
  const options = ref([])
  const currentPage = ref(1)
  const itemsPerPage = 15

  const changeOption = function (saving, type, trm) {
      return options.value.filter((option) => option.saving == saving.id && option.rsrv_type_nm == type && option.save_trm == trm)
  }

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

  onMounted(() => {
  store.getSaving()
    .then(() => {
      savings.value = store.savings
      options.value = store.savingoptions
    })
    .catch(err => {
      console.error('데이터 로딩 실패:', err)
    })
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
  