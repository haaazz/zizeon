<template>
    <div>
      <container>
            <h1>내 주변 은행 찾기</h1>
        <div>
            <btn>
                <select v-model="province" @change="updateCities">
                <option value="">도/시</option>
                <option v-for="info in infos" :key="info.id">
                    {{ info.prov }}
                </option>
                </select>
            </btn>　
            <btn>
                <select v-model="city">
                <option value="">시/군/구</option>
                <option v-for="c in cities" :key="c">{{ c }}</option>
                </select>
            </btn>　
            <btn>
                <select v-model="bank">
                <option value="">은행명</option>
                <option v-for="b in banks" :key="b">{{ b }}</option>
                </select>
            </btn>
        </div>
          <div>
            <MapComponent :province="province" :city="city" :bank="bank" />
          </div>

      </container>
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
  
  <style scoped>
  * {
    font-family: YeongjuSeonbi;
  }
  container {
    text-align: center;
  }
  </style>