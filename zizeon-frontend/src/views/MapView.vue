<template>
  <div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8">
    <div class="mx-auto max-w-lg">
      <h1 class="text-center text-2xl font-bold text-green-600 sm:text-3xl">
        내 주변 은행 찾기💸
      </h1>


        <div class="text-center">
            <select v-model="province" @change="updateCities" class="mt-8 w-1/5 rounded-lg border-gray-500 text-gray-700 sm:text-sm p-2 border border-gray-300 mr-3">
              <option value="">도/시</option>
              <option v-for="info in infos" :key="info.id">
                {{ info.prov }}
              </option>
            </select>

            <select v-model="city"  class="mt-8 w-1/5 rounded-lg border-gray-500 text-gray-700 sm:text-sm p-2 border border-gray-300 mr-3">
              <option value="">시/군/구</option>
              <option v-for="c in cities" :key="c">{{ c }}</option>
            </select> 

            <select v-model="bank"  class="mt-8 w-1/5 rounded-lg border-gray-500 text-gray-700 sm:text-sm p-2 border border-gray-300">
              <option value="">은행명</option>
              <option v-for="b in banks" :key="b">{{ b }}</option>
            </select>
          

          <div>
            <MapComponent :province="province" :city="city" :bank="bank" />
          </div>
        </div>
      </div>
    </div>
</template>

<script setup lang="ts">
import MapComponent from "@/components/MapComponent.vue";
import { ref, watch } from "vue";
import { useMapStore } from "@/stores/map";

const store = useMapStore();

const infos = store.infos;
const banks = store.banks;
const cities = ref<string[]>([]);

const province = ref("");
const city = ref("");
const bank = ref("");

const updateCities = () => {
  const selectedInfo = infos.find((info) => info.prov === province.value);
  cities.value = selectedInfo ? selectedInfo.city : [];
};

watch(province, () => {
  updateCities();
});
</script>
<style scoped></style>
