<template>
    <div class="map-component-under">
      <button @click="searchOnMap">검색하기</button>
      <div id="mapContainer"></div>
    </div>
  </template>
  
  <script lang="ts">
  declare global {
    interface Window {
      kakao: any;
    }
  }
  export default {
    name: "KakaoMap",
    beforeDestroy() {
      window.removeEventListener("resize", handleWindowResize);
    },
  };
  </script>
  
  <script setup lang="ts">
  import { onMounted, ref } from "vue";
  
  const props = defineProps({
    province: String,
    city: String,
    bank: String,
  });
  
  const map = ref();
  const infowindow = ref();
  const markers = ref<any[]>([]);
  const searchKeyword = ref("");
  
  const loadKakaoMap = function () {
    const script = document.createElement("script");
    const KAKAO_KEY = import.meta.env.VITE_KAKAO_KEY;
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${KAKAO_KEY}&autoload=false&libraries=services`;
    script.async = true;
    script.onload = () => {
      window.kakao.maps.load(function () {
        initializeKakaoMap();
      });
    };
  
    document.head.appendChild(script);
  };
  
  const initializeKakaoMap = function () {
    console.log("Initializing Kakao Map");
    const mapContainer = document.querySelector("#mapContainer");
    const mapOption = {
      center: new window.kakao.maps.LatLng(37.566826, 126.9786567),
      level: 3,
    };
  
    map.value = new window.kakao.maps.Map(mapContainer, mapOption);
    infowindow.value = new window.kakao.maps.InfoWindow({ zIndex: 1 });
  };
  
  const handleWindowResize = function () {
    if (map) {
      map.value.relayout();
    }
  };
  
  onMounted(() => {
    loadKakaoMap();
    window.addEventListener("resize", handleWindowResize);
  });
  
  const searchOnMap = function () {
    console.log("Button clicked");
    map.value.isLoading = true;
    searchKeyword.value = `${props.province} ${props.city} ${props.bank}`;
    console.log("Search Keyword:", searchKeyword);
    searchPlaces(searchKeyword.value);
  };
  
  const searchPlaces = function (keyword: any) {
    const ps = new window.kakao.maps.services.Places();
  
    ps.keywordSearch(keyword, placesSearchCB);
  };
  
  const placesSearchCB = function (data: any, status: any, pagination: any) {
    if (status === window.kakao.maps.services.Status.OK) {
      removeAllMarkers();
      var bounds = new window.kakao.maps.LatLngBounds();
  
      for (var i = 0; i < data.length; i++) {
        displayMarker(data[i]);
        bounds.extend(new window.kakao.maps.LatLng(data[i].y, data[i].x));
      }
      map.value.setBounds(bounds);
      infowindow.value.close();
    } else {
      alert("선택한 지역에 해당 은행이 없습니다. 다른 은행을 선택해주세요.");
    }
  };
  
  const displayMarker = function (place: any) {
    const marker = new window.kakao.maps.Marker({
      map: map.value,
      position: new window.kakao.maps.LatLng(place.y, place.x),
    });
  
    window.kakao.maps.event.addListener(marker, "click", () => {
      infowindow.value.setContent(
        '<div style="padding:5px;font-size:11px;">' + place.place_name + "</div>"
      );
      infowindow.value.open(map.value, marker);
    });
  
    markers.value.push(marker);
  };
  
  const removeAllMarkers = function () {
    for (let i = 0; i < markers.value.length; i++) {
      markers.value[i].setMap(null);
    }
    markers.value = [];
  };
  </script>
  
  <style scoped>
  button {
    text-align: center;
    margin: 15px;
  }
  #mapContainer {
    width: 80%;
    height: 550px;
    margin: auto;
  }
  * {
    font-family: YeongjuSeonbi;
  }
  </style>