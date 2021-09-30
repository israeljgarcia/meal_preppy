<!-- src/components/Courses.vue -->
<template>
  <div class="container">
    <b-modal
      ref="addCourseModal"
      id="course-modal"
      title="Add a new course"
      hide-footer
    >
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group
          id="form-title-group"
          label="Title:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            type="text"
            v-model="addCourseForm.title"
            required
            placeholder="Enter title"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="Author:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            type="text"
            v-model="addCourseForm.author"
            required
            placeholder="Enter author"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group
            v-model="addCourseForm.paperback"
            id="form-checks"
          >
            <b-form-checkbox value="true">Paperback</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

    <h1>Courses</h1>
    <hr />
    <button type="button" class="btn btn-success btn-sm" v-b-modal.course-model>
      Add Course
    </button>
    <table class="table table-hover">
      <tr>
        <th scope="col">Title</th>
        <th scope="col">Author</th>
        <th scope="col">Paperback</th>
      </tr>
      <tbody>
        <tr v-for="(course, index) in courses" :key="index">
          <td>{{ course.title }}</td>
          <td>{{ course.author }}</td>
          <td>
            <span v-if="course.paperback">Yes</span>
            <span v-else>No</span>
          </td>
          <td>
            <button type="button" class="btn btn-info btn-sm">
              Update
            </button>
            <button type="button" class="btn btn-danger btn-sm">
              Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<!-- src/components/Courses.vue -->

<script>
import axios from 'axios';

export default {
  name: 'Course',
  data() {
    return {
      courses: [],
      addCourseForm: {
        title: '',
        author: '',
        paperback: [],
      },
    };
  },
  methods: {
    getCourses() {
      const path = 'http://localhost:5000/courses';
      axios
        .get(path)
        .then((res) => {
          this.courses = res.data.courses;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addCourse(payload) {
      const path = 'http://localhost:5000/courses';
      axios
        .post(path, payload)
        .then(() => {
          this.getCourses();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getCourses();
        });
    },
    initForm() {
      this.addCourseForm.title = '';
      this.addCourseForm.author = '';
      this.addCourseForm.paperback = [];
    },
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addCourseModal.hide();
      let paperback = false;
      if (this.addCourseForm.paperback[0]) paperback = true;
      const payload = {
        title: this.addCourseForm.title,
        author: this.addCourseForm.author,
        paperback,
      };
      this.addCourse(payload);
      this.initForm();
    },
  },
  created() {
    this.getCourses();
  },
};
</script>
