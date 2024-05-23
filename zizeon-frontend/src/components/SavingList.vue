<template>
  <div class="content">
    <h3 class="text-2xl font-bold sm:text-4xl mb-4 text-center mt-8">
      적금 상품 조회
    </h3>

    <div class="flex justify-between mb-8 ml-5 mr-5">
      <div class="max-w-sm">
        <label for="bankFilter">찾으시려는 은행을 선택해주세요.</label>
        <select
          id="bankFilter"
          v-model="selectedBank"
          @change="filterSavings"
          class="block px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer"
        >
          <option selected>전체</option>
          <option v-for="bank in uniqueBanks" :key="bank" :value="bank">
            {{ bank }}
          </option>
        </select>
      </div>

      <button
        @click="resetFiltersAndSorting"
        class="mt-0 mr-0 rounded bg-green-600 px-2 py-1 text-xs text-white transition hover:bg-green-700 focus:outline-none"
      >
        필터링 초기화
      </button>
    </div>
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
              적립유형명
            </th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
              회사명
            </th>
            <th
              @click="sortSavings(6)"
              class="whitespace-nowrap px-4 py-2 font-medium text-gray-900"
            >
              6개월
            </th>
            <th
              @click="sortSavings(12)"
              class="whitespace-nowrap px-4 py-2 font-medium text-gray-900"
            >
              12개월
            </th>
            <th
              @click="sortSavings(24)"
              class="whitespace-nowrap px-4 py-2 font-medium text-gray-900"
            >
              24개월
            </th>
            <th
              @click="sortSavings(36)"
              class="whitespace-nowrap px-4 py-2 font-medium text-gray-900"
            >
              36개월
            </th>
          </tr>
        </thead>

        <tbody class="divide-y divide-gray-200">
          <tr v-for="saving in paginatedSavings" :key="saving.id">
            <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
              {{ saving.id }}
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              <RouterLink
                :to="{ name: 'SavingDetail', params: { id: saving.id } }"
                >{{ saving.fin_prdt_nm }}</RouterLink
              >
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              {{ saving.kor_co_nm }}
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              자유적립식
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              {{ getInterestRate(saving, "자유적립식", 6) }}
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              {{ getInterestRate(saving, "자유적립식", 12) }}
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              {{ getInterestRate(saving, "자유적립식", 24) }}
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              {{ getInterestRate(saving, "자유적립식", 36) }}
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

<style scoped></style>
