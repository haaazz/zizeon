<template>
  <div class="content">
    <h1>적금</h1>
    <div>
      <label for="bankFilter">은행 선택: </label>
      <select id="bankFilter" v-model="selectedBank" @change="filterSavings">
        <option value="">전체</option>
        <option v-for="bank in uniqueBanks" :key="bank" :value="bank">
          {{ bank }}
        </option>
      </select>
      <button @click="resetFiltersAndSorting">초기화</button>
    </div>
    <table>
      <thead>
        <tr>
          <th>번호</th>
          <th>상품명</th>
          <th>회사명</th>
          <th>적립유형명</th>
          <th @click="sortSavings(6)">6개월</th>
          <th @click="sortSavings(12)">12개월</th>
          <th @click="sortSavings(24)">24개월</th>
          <th @click="sortSavings(36)">36개월</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="saving in paginatedSavings" :key="saving.id">
          <td>{{ saving.id }}</td>
          <td>
            <RouterLink
              :to="{ name: 'SavingDetail', params: { id: saving.id } }"
              >{{ saving.fin_prdt_nm }}</RouterLink
            >
          </td>
          <td>{{ saving.kor_co_nm }}</td>
          <td>자유적립식</td>
          <td>{{ getInterestRate(saving, "자유적립식", 6) }}</td>
          <td>{{ getInterestRate(saving, "자유적립식", 12) }}</td>
          <td>{{ getInterestRate(saving, "자유적립식", 24) }}</td>
          <td>{{ getInterestRate(saving, "자유적립식", 36) }}</td>
        </tr>
      </tbody>
    </table>
    <div class="pagination">
      <button @click="prevPage" :disabled="currentPage === 1">이전</button>
      <span>{{ currentPage }} / {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">
        다음
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useSavingStore } from "@/stores/saving";
import { RouterLink } from "vue-router";

const store = useSavingStore();
const savings = ref([]);
const filteredSavings = ref([]);
const options = ref([]);
const currentPage = ref(1);
const itemsPerPage = 15;
const selectedBank = ref("");

const resetFiltersAndSorting = () => {
  selectedBank.value = "";
  sortOrder.value = {
    6: null,
    12: null,
    24: null,
    36: null,
  };
  currentPage.value = 1;
  filterSavings();

  filteredSavings.value.sort((a, b) => a.id - b.id);
};

const uniqueBanks = computed(() => {
  const banks = savings.value.map((saving) => saving.kor_co_nm);
  return [...new Set(banks)];
});

const filterSavings = () => {
  if (selectedBank.value) {
    filteredSavings.value = savings.value.filter(
      (saving) => saving.kor_co_nm === selectedBank.value
    );
  } else {
    filteredSavings.value = savings.value;
  }
};

const getInterestRate = (saving, type, trm) => {
  const option = options.value.find(
    (option) =>
      option.saving === saving.id &&
      option.rsrv_type_nm === type &&
      option.save_trm === trm
  );
  return option ? option.intr_rate : "-";
};

const totalPages = computed(() => {
  return Math.ceil(filteredSavings.value.length / itemsPerPage);
});

const paginatedSavings = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return filteredSavings.value.slice(start, end);
});

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

const sortOrder = ref({
  6: null,
  12: null,
  24: null,
  36: null,
});

const sortSavings = (term) => {
  const order = sortOrder.value[term] === "asc" ? "desc" : "asc";
  sortOrder.value[term] = order;

  filteredSavings.value.sort((a, b) => {
    const aRate = parseFloat(getInterestRate(a, "자유적립식", term)) || 0;
    const bRate = parseFloat(getInterestRate(b, "자유적립식", term)) || 0;
    return order === "asc" ? aRate - bRate : bRate - aRate;
  });
};

onMounted(() => {
  store
    .getSaving()
    .then(() => {
      savings.value = store.savings;
      options.value = store.savingoptions;
      filterSavings();
    })
    .catch((err) => {
      console.error("데이터 로딩 실패:", err);
    });
});
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

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}

th {
  background-color: #f2f2f2;
  cursor: pointer;
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
