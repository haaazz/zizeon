<template>
  <div class="content">
    <h3 class="text-2xl font-bold sm:text-4xl mb-4 text-center mt-8">
      예금 상품 조회
    </h3>

    <div class="max-w-sm">
      <label for="bankFilter">찾으시려는 은행을 선택해주세요.</label>
      <select
        id="bankFilter"
        v-model="selectedBank"
        @change="filterDeposits"
        class="block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer"
      >
        <option selected>전체</option>
        <option v-for="bank in uniqueBanks" :key="bank" :value="bank">
          {{ bank }}
        </option>
      </select>
    </div>
    <button
      @click="resetFiltersAndSorting"
      class="mt-0 mr-0 rounded bg-green-600 px-5 py-2 text-sm text-white transition hover:bg-green-700 focus:outline-none"
    >
      필터링 초기화
    </button>
  </div>

  <div class="rounded-lg border border-gray-200">
    <div class="overflow-x-auto rounded-t-lg">
      <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
        <thead class="ltr:text-left rtl:text-right">
          <tr>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
              번호
            </th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
              상품명
            </th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
              회사명
            </th>
            <th
              @click="sortDeposits(12)"
              class="whitespace-nowrap px-4 py-2 font-medium text-gray-900"
            >
              6개월
            </th>
            <th
              @click="sortDeposits(12)"
              class="whitespace-nowrap px-4 py-2 font-medium text-gray-900"
            >
              12개월
            </th>
            <th
              @click="sortDeposits(24)"
              class="whitespace-nowrap px-4 py-2 font-medium text-gray-900"
            >
              24개월
            </th>
            <th
              @click="sortDeposits(36)"
              class="whitespace-nowrap px-4 py-2 font-medium text-gray-900"
            >
              36개월
            </th>
          </tr>
        </thead>

        <tbody class="divide-y divide-gray-200">
          <tr v-for="deposit in paginatedDeposits" :key="deposit.id">
            <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
              {{ deposit.id }}
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              <RouterLink
                :to="{ name: 'DepositDetail', params: { id: deposit.id } }"
                >{{ deposit.fin_prdt_nm }}</RouterLink
              >
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              {{ deposit.kor_co_nm }}
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              {{ getInterestRate(deposit, 6) }}
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              {{ getInterestRate(deposit, 12) }}
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              {{ getInterestRate(deposit, 24) }}
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              {{ getInterestRate(deposit, 36) }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="text-center mt-8">
    <button @click="prevPage" :disabled="currentPage === 1">이전</button>
    <span class="mr-2 ml-2">{{ currentPage }} / {{ totalPages }}</span>
    <button @click="nextPage" :disabled="currentPage === totalPages">
      다음
    </button>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useDepositStore } from "@/stores/deposit";
import { RouterLink } from "vue-router";

const store = useDepositStore();
const deposits = ref([]);
const filteredDeposits = ref([]);
const options = ref([]);
const currentPage = ref(1);
const itemsPerPage = 15;
const selectedBank = ref("");

const uniqueBanks = computed(() => {
  const banks = deposits.value.map((deposit) => deposit.kor_co_nm);
  return [...new Set(banks)];
});

const filterDeposits = () => {
  if (selectedBank.value) {
    filteredDeposits.value = deposits.value.filter(
      (deposit) => deposit.kor_co_nm === selectedBank.value
    );
  } else {
    filteredDeposits.value = deposits.value;
  }
  currentPage.value = 1;
};

const getInterestRate = (deposit, term) => {
  const option = options.value.find(
    (option) =>
      option.fin_prdt_cd === deposit.fin_prdt_cd &&
      option.save_trm === term.toString()
  );
  return option ? option.intr_rate : "-";
};

const totalPages = computed(() => {
  return Math.ceil(filteredDeposits.value.length / itemsPerPage);
});

const paginatedDeposits = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return filteredDeposits.value.slice(start, end);
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

const sortDeposits = (term) => {
  const order = sortOrder.value[term] === "asc" ? "desc" : "asc";
  sortOrder.value[term] = order;

  filteredDeposits.value.sort((a, b) => {
    const aRate = parseFloat(getInterestRate(a, term)) || 0;
    const bRate = parseFloat(getInterestRate(b, term)) || 0;
    return order === "asc" ? aRate - bRate : bRate - aRate;
  });
};

const resetFiltersAndSorting = () => {
  selectedBank.value = "";
  sortOrder.value = {
    6: null,
    12: null,
    24: null,
    36: null,
  };
  currentPage.value = 1;
  filterDeposits();

  // 금리 정렬 초기화
  Object.keys(sortOrder.value).forEach((term) => {
    sortOrder.value[term] = null;
  });

  // 예금 번호를 기준으로 정렬
  filteredDeposits.value.sort((a, b) => a.id - b.id);
};
onMounted(async () => {
  await store.getDeposit();
  deposits.value = store.deposits;
  options.value = store.depositoptions;
  filterDeposits();
});
</script>

<style scoped></style>
