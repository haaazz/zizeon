<template>

  <div class="text-center w-3/4 flex justify-center mx-auto">
    <button
      class="mt-8 mr-2 inline-block rounded bg-green-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-green-700 focus:outline-none focus:ring focus:ring-yellow-400"
      @click="selectTab('deposit')"
    >
      예금 상품 조회
    </button>
    <button
      class="mt-8 ml-2 inline-block rounded bg-green-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-green-700 focus:outline-none focus:ring focus:ring-yellow-400"
      @click="selectTab('saving')"
    >
      적금 상품 조회
    </button>
  </div>

  <div>
    <DepositList v-if="currentTab === 'deposit'" />
    <SavingList v-if="currentTab === 'saving'" />
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import DepositList from "@/components/DepositList.vue";
import SavingList from "@/components/SavingList.vue";

const route = useRoute();
const router = useRouter();

const currentTab = ref(route.query.tab || "deposit");

const selectTab = (tab) => {
  currentTab.value = tab;
  router.push({ query: { tab } });
};

watch(route, (newRoute) => {
  currentTab.value = newRoute.query.tab || "deposit";
});
</script>

<style scoped></style>
