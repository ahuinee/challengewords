<template>
  <div class="grade">
    <el-container>
      <el-header>
        <h1>选择年级</h1>
      </el-header>
      <el-main>
        <!-- 年级选择 -->
        <div v-for="(item, index) in grades" :key="index">
          <el-radio
            style="margin-top: 10px"
            v-model="selectedGradeIndex"
            :label="index"
            >{{ item.gradeName }}</el-radio
          >
        </div>

        <!-- 下一步 选择学期 -->
        <el-button
          style="margin: 100px"
          type="primary"
          round
          @click="pushVolume"
          >下一步</el-button
        >
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Grade",
  data() {
    return {
      grades: [],
      selectedGradeIndex: 0,
    };
  },
  created() {
    this.grades = this.$route.params.grades;
  },
  methods: {
    // 进入学期选择
    pushVolume() {
      const volumes = this.grades[this.selectedGradeIndex].volumes;
      console.log(volumes);
      this.$router.push({ name: "Volume", params: { volumes: volumes } });
    },
  },
};
</script>
