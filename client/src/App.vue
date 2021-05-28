<!--
  MAIN PAGE
-->
<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Contatos telefônicos</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.manage-contact-modal>Novo contato</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Nome</th>
              <th scope="col">Telefone</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(contact, index) in contacts" :key="index">
              <td>{{ contact.id }}</td>
              <td>{{ contact.contact_name }}</td>
              <td>{{ contact.contact_phone }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <b-modal ref="manageContactModal" id="manage-contact-modal" title="Novo contato" hide-footer>
      <b-form @submit="onSubmit" class="w-100">
        <b-form-group id="form-name-group" label="Nome:" label-for="form-name-input">
          <b-form-input id="form-name-input" type="text" v-model="addContactForm.name" required placeholder="Nome do contato"></b-form-input>
        </b-form-group>
        <b-form-group id="form-tel-number-group" label="Telefone:" label-for="form-tel-number-input">
          <b-form-input id="form-tel-number-input" type="text" v-model="addContactForm.number" required placeholder="Número de telefone"></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Salvar</b-button>
      </b-form>
    </b-modal>
  </div>
</template>


<!--
  SCRIPTS THAT WILL INTERACT WITH BACKEND
-->
<script>
import axios from 'axios';
//import VueAxios from 'vue-axios'
export default {
  data() {
    return {
      contacts: [],
      addContactForm: {
        name: '',
        number: ''
      }
    };
  },
  methods: {
    
    /**
     * List all contacts registered in DB
    */
    listContacts() {
      const path = location.protocol + '//' + location.hostname + ':5000/';
      axios.get(path)
        .then((res) => {
          this.contacts = res.data.json_list;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    /**
     * Callback to request to add a new contact on backend
     * 
     * @param {object} data Contains the form content
    */
    addContact(data) {
      const path = location.protocol + '//' + location.hostname + 
        ':5000/new/?contact_name=' + data.name + '&contact_phone=' + data.number;

      axios.post(path)
        .then(() => {
          this.listContacts();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);

          this.listContacts();
        });
    },
    initForm() {
      this.addContactForm.name = '';
      this.addContactForm.number = '';
    },
    /**
     * New contact submit callback
     * 
     * @param {object} evt The modal submit event 
    */
    onSubmit(evt) {
      evt.preventDefault(); // Handle any other request
      this.$refs.manageContactModal.hide();

      const data = {
        name: this.addContactForm.name,
        number: this.addContactForm.number
      };

      // Request and update list
      this.addContact(data);
      this.initForm();
    }
  },
  created() {
    this.listContacts();
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
