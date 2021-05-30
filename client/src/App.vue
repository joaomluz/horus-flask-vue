<!--
  MAIN PAGE
-->
<template>
  <div class="container">
    <!--
      Main table
    -->
    <div class="row">
      <div class="col-sm-10">
        <h1>Contatos telefônicos</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.manage-contact-modal>Novo contato</button>
        <br><br>

        <!-- 
          Action - returned status
        -->
        <alert :message="message" v-if="displayStatus"></alert>

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
                  <button type="button" class="btn btn-danger btn-sm" @click="onDelete(contact)">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 
      Modal for add new user
    -->
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
import Alert from './components/Alert.vue';

export default {
  data() {
    return {
      contacts: [],
      addContactForm: {
        name: '',
        number: ''
      },
      message: '',
      displayStatus: false
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
        .then((response) => {
          this.listContacts();
          if (response.data.status) {
            this.message = "Contato criado com sucesso";
          } else {
            this.message = response.data.error;
          }

          this.displayStatus = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);

          this.listContacts();
        });
    },
    /**
     * Removes contact with given ID
     * 
     * @param {int} id Contact UID
    */
    rmContact(id) {
      const path = location.protocol + '//' + location.hostname + 
        ':5000/update/' + id + '?method=delete';

      axios.get(path)
        .then((response) => {
          this.listContacts();
          if (response.data.status) {
            this.message = "Contato removido";
          } else {
            this.message = response.data.error;
          }

          this.displayStatus = true;
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
    },
    /**
     * Handle delete contact button
     * 
     * @param {object} element clicked element
    */
    onDelete(contact) {
      this.rmContact(contact.id)
    }
  },
  created() {
    this.listContacts();
  },
  components: {
    alert: Alert
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
