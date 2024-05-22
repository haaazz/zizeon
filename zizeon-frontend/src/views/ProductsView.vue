<template>
  <div class="container">
    <div class="selectbtn">
      <button @click="selectTab('deposit')">예금</button>
      <button @click="selectTab('saving')">적금</button>
    </div>
    <div class="content">
      <DepositList v-if="currentTab === 'deposit'" />
      <SavingList v-if="currentTab === 'saving'" />
    </div>
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

<style scoped>
.container {
  display: flex;
  flex-direction: column;
}

.selectbtn {
  text-align: center;
  margin-bottom: 20px;
}

button {
  margin: 0 10px;
  padding: 10px 20px;
  cursor: pointer;
}

button:focus {
  outline: none;
}

.content {
  display: flex;
  justify-content: center;
  width: 100%;
}

* {
  font-family: YeongjuSeonbi;
}
</style>
