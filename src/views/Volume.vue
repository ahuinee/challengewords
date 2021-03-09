<template>
  <div>
    <el-container>
      <el-header>
        <h1>选择学期</h1>
      </el-header>
      <el-main>
        <!-- 学期选择 -->
        <div v-for="(item, index) in volumes" :key="index">
          <el-radio
            style="margin-top: 10px"
            v-model="selectedVolumeIndex"
            :label="index"
            >{{ item.volumeName }}</el-radio
          >
        </div>

        <!-- 下一步 选择单元 -->
        <el-button style="margin: 100px" type="primary" round @click="pushUnit"
          >下一步</el-button
        >
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Volume",
  data() {
    return {
      volumes: [],
      selectedVolumeIndex: 0,
    };
  },
  created() {
    this.volumes = this.$route.params.volumes;
  },
  methods: {
    // 进入单元选择
    pushUnit() {
      const units = this.volumes[this.selectedVolumeIndex].units;
      console.log(units);
      this.$router.push({ name: "Uint", params: { units: units } });
    },
  },
};
</script>
