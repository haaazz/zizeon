<template>
  <div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8">
    <div class="mx-auto w-3/4">
      <h1
        class="text-center text-2xl font-bold text-green-600 sm:text-3xl mb-16"
      >
        환율 계산💸
      </h1>

      <div class="flex justify-around items-end">
        <div>
          <label
            for="nation"
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
            >국가/통화명 선택</label
          >

          <select v-model="nation" class="p-2 border rounded-lg">
            <option
              v-for="currency in store.currencies"
              :key="currency.id"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            >
              {{ currency.cur_nm }}
            </option>
          </select>
        </div>

        <div>
          <label
            for="foreign"
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
            >외화 입력</label
          >
          <input
            type="number"
            v-model="foreign"
            class="p-1 border rounded-lg"
          />
          <button
            @click="convertToKRW"
            class="p-1 border rounded-lg bg-slate-100"
          >
            환전
          </button>
        </div>

        <div>
          <label
            for="KRW"
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
            >한화 입력</label
          >
          <input type="number" v-model="KRW" class="p-1 border rounded-lg" />
          <button
            @click="convertToForeign"
            class="p-1 border rounded-lg bg-slate-100"
          >
            환전
          </button>
        </div>
        <button
          @click="resetExchange"
          class="mt-0 mr-0 rounded bg-green-600 px-2 py-1 text-xs text-white transition hover:bg-green-700 focus:outline-none h-8"
        >
          초기화
        </button>
      </div>

      <hr class="mt-5" />
      <br />
      <table
        class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm mt-5"
      >
        <thead class="ltr:text-left rtl:text-right">
          <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
            국가/통화명
          </th>
          <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
            전신환(송금) 받을 때
          </th>
          <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
            매매 기준율
          </th>
          <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
            전신환(송금) 보낼 때
          </th>
          <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
            장부가격
          </th>
        </thead>
        <tbody class="divide-y divide-gray-200">
          <tr v-for="currency in store.currencies" :key="currency.id">
            <td
              class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center"
            >
              {{ currency.cur_nm }}
            </td>
            <td
              class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center"
            >
              {{ currency.deal_bas_r }}
            </td>
            <td
              class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center"
            >
              {{ currency.ttb }}
            </td>
            <td
              class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center"
            >
              {{ currency.tts }}
            </td>
            <td
              class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center"
            >
              {{ currency.bkpr }}
            </td>
          </tr>
        </tbody>
      </table>
      <br />
      <p class="text-end text-xs">환율은 매일 오전 10시에 업데이트됩니다.</p>
      <br />
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import { onMounted, ref, watch, computed } from "vue";

const store = useCounterStore();
onMounted(() => {
  store.getCurrency();
});

const nation = ref(null);
const currency = computed(() => {
  return store.currencies.find((currency) => currency.cur_nm === nation.value);
});

const KRW = ref(0);
const foreign = ref(0);

const convertToForeign = () => {
  if (currency.value) {
    foreign.value = KRW.value / currency.value.deal_bas_r.replace(/,/g, "");
  }
};

const convertToKRW = () => {
  if (currency.value) {
    KRW.value = foreign.value * currency.value.deal_bas_r.replace(/,/g, "");
  }
};

const resetExchange = () => {
  KRW.value = 0;
  foreign.value = 0;
  nation.value = null;
};
</script>

<style scoped></style>
