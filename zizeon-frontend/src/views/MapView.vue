<template>
    <div id="map-container">
        <div id="map"></div>
    </div>
</template>

<script>
    export default {
        mounted() {
            const API_KEY = import.meta.env.VITE_API_KEY

            if (!window.kakao || !window.kakao.maps) {
                const script = document.createElement('script')
                script.type = 'text/javascript'
                script.src =
                    '//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=' + API_KEY + '&libraries=clusterer,drawing,services'
                script.addEventListener('load', () => {
                    kakao.maps.load(() => {
                    this.initMap()
                    })
                })
                document.head.appendChild(script)
            } else {
                this.initMap()
            }
        },
        methods: {
            initMap() {
            const container = document.getElementById('map')
            const options = {
                center: new kakao.maps.LatLng(33.450701, 126.570667),
                level: 8
            }
            this.map = new kakao.maps.Map(container, options)
            }
        }
    }
</script>

<style scoped>
#map-container {
    display: flex;
    margin: auto;
    justify-content: center;
    align-items: center;
    margin-left: 1000px;
    height: 80vh; /* 화면 전체 높이에 지도를 중앙에 배치 */
}

#map {
    width: 550px;
    height: 450px;
}
</style>