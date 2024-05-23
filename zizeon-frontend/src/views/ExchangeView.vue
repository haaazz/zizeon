<template>
  <div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8 mt-12">
    <div class="mx-auto max-w-lg">
      <h1 class="text-center text-2xl font-bold text-green-600 sm:text-3xl mb-16">
        환율 계산💸
      </h1>
      <div>
        <select v-model="nation">
          <option v-for="currency in store.currencies" :key="currency.id">
            {{ currency.cur_nm }}
          </option>
        </select>
        <input type="number" v-model="foreign" />
        <button @click="convertToKRW" class="ml-20">$</button>
        <input type="number" v-model="KRW" />
        <button @click="convertToForeign">₩</button>
      </div>
      <br>
      <table>
        <thead>
          <tr>
            <th>국가/통화명</th>
            <th>전신환(송금) 받을 때</th>
            <th>매매 기준율</th>
            <th>전신환(송금) 보낼 때</th>
            <th>장부가격</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="currency in store.currencies" :key="currency.id">
            <td>{{ currency.cur_nm }}</td>
            <td>{{ currency.deal_bas_r }}</td>
            <td>{{ currency.ttb }}</td>
            <td>{{ currency.tts }}</td>
            <td>{{ currency.bkpr }}</td>
          </tr>
        </tbody>
      </table>
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
</script>

<style scoped></style>
