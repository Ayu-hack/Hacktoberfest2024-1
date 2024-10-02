using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PharmacyManagementSystem
{
    public partial class Medicines : Form
    {
        public Medicines()
        {
            InitializeComponent();
            ShowMed();
            GetManufacturer();
        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {
            
        }
        SqlConnection conn = new SqlConnection(@"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\syedm\OneDrive\Documents\PharmacySystemDB.mdf;Integrated Security=True;Connect Timeout=30");
       
        private void ShowMed()
        {
            conn.Open();
            string query = "Select * from MedicineTbl";
            SqlDataAdapter sda = new SqlDataAdapter(query, conn);
            SqlCommandBuilder Builder = new SqlCommandBuilder(sda);
            var ds = new DataSet();
            sda.Fill(ds);
            MedicinesDGV.DataSource = ds.Tables[0];


            conn.Close();
        }
        private void Reset()
        {
            MedicineManfactNameTb.Text = "";
            MedicineNameTb.Text = "";
            MedicinePriceTb.Text = "";
            MedicineQuantityTb.Text = "";
            MedicineTypeCb.SelectedIndex = 0;
            key = 0;
            
        }
        private void GetManufacturer()
        {
            conn.Open();
            SqlCommand cmd = new SqlCommand("Select ManfacId from ManufacturerTbl ",conn);
            SqlDataReader Rdr;
            Rdr = cmd.ExecuteReader();
            DataTable dt = new DataTable();
            dt.Columns.Add("ManfacId", typeof(int));
            dt.Load(Rdr);
            MedicineManfactCb.ValueMember = "ManfacId";
            MedicineManfactCb.DataSource = dt;

            conn.Close();
        }
        private void GetManufacturerName()
        {
            conn.Open();
            string query = "Select * from ManufacturerTbl where ManfacId='"+MedicineManfactCb.SelectedValue.ToString()+"'";
            SqlCommand cmd = new SqlCommand(query, conn);
            DataTable dt = new DataTable();
            SqlDataAdapter sda = new SqlDataAdapter(cmd);
            sda.Fill(dt);
            foreach(DataRow dr in dt.Rows)
            {
                MedicineManfactNameTb.Text = dr["ManfacName"].ToString();

            }


            conn.Close();
        }
        private void SaveBtn_Click(object sender, EventArgs e)
        {
            if (MedicineNameTb.Text == "" || MedicinePriceTb.Text == "" || MedicineQuantityTb.Text == "" || MedicineTypeCb.SelectedIndex == -1 || MedicineManfactNameTb.Text=="" )
            {
                MessageBox.Show("Missing Information!!");
            }
            else
            {
                try
                {
                    conn.Open();
                    SqlCommand cmd = new SqlCommand("insert into MedicineTbl(MedicineName,MedicineType,MedicineQuantity,MedicinePrice,MedicineManId,MedicineManufact)values(@MN,@MT,@MQ,@MP,@MMI,@MM)", conn);
                    cmd.Parameters.AddWithValue("@MN", MedicineNameTb.Text);
                    cmd.Parameters.AddWithValue("@MT", MedicineTypeCb.SelectedItem.ToString());
                    cmd.Parameters.AddWithValue("@MQ", MedicineQuantityTb.Text);
                    cmd.Parameters.AddWithValue("@MP", MedicinePriceTb.Text);
                    cmd.Parameters.AddWithValue("@MMI", MedicineManfactCb.SelectedValue.ToString());
                    cmd.Parameters.AddWithValue("@MM", MedicineManfactNameTb.Text);
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("Medicine Added Successfully");



                    conn.Close();
                    ShowMed();
                    Reset();

                }
                catch (Exception Ex)
                {
                    MessageBox.Show(Ex.Message);
                }

            }
        }

        private void MedicineManfactCb_SelectionChangeCommitted(object sender, EventArgs e)
        {
            GetManufacturerName();
        }

        int key = 0;
        private void MedicinesDGV_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            MedicineNameTb.Text = MedicinesDGV.SelectedRows[0].Cells[1].Value.ToString();
            MedicineTypeCb.SelectedItem = MedicinesDGV.SelectedRows[0].Cells[2].Value.ToString();
            MedicineQuantityTb.Text = MedicinesDGV.SelectedRows[0].Cells[3].Value.ToString();
            MedicinePriceTb.Text = MedicinesDGV.SelectedRows[0].Cells[4].Value.ToString();
            MedicineManfactCb.SelectedValue = MedicinesDGV.SelectedRows[0].Cells[5].Value.ToString();
            MedicineManfactNameTb.Text = MedicinesDGV.SelectedRows[0].Cells[6].Value.ToString();


            if (MedicineNameTb.Text == "")
            {
                key = 0;

            }
            else
            {
                key = Convert.ToInt32(MedicinesDGV.SelectedRows[0].Cells[0].Value.ToString());
            }
        }

        private void DeleteBtn_Click(object sender, EventArgs e)
        {
            if (key == 0)
            {
                MessageBox.Show("Select the Medicine!!");
            }
            else
            {
                try
                {
                    conn.Open();
                    SqlCommand cmd = new SqlCommand("Delete from MedicineTbl where MedicineNum=@Mkey", conn);
                    cmd.Parameters.AddWithValue("@Mkey", key);
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("Medicine Remove Successfully");


                    conn.Close();
                    ShowMed();
                    Reset();

                }
                catch (Exception Ex)
                {
                    MessageBox.Show(Ex.Message);
                }

            }
        }

        private void EditBtn_Click(object sender, EventArgs e)
        {

            if (MedicineNameTb.Text == "" || MedicinePriceTb.Text == "" || MedicineQuantityTb.Text == "" || MedicineTypeCb.SelectedIndex == -1 || MedicineManfactNameTb.Text == "")
            {
                MessageBox.Show("Missing Information!!");
            }
            else
            {
                try
                {
                    conn.Open();
                    SqlCommand cmd = new SqlCommand("Update MedicineTbl Set MedicineName=@MN,MedicineType=@MT,MedicineQuantity=@MQ,MedicinePrice=@MP,MedicineManId=@MMI,MedicineManufact=@MM where MedicineNum=@Mkey", conn);
                    cmd.Parameters.AddWithValue("@MN", MedicineNameTb.Text);
                    cmd.Parameters.AddWithValue("@MT", MedicineTypeCb.SelectedItem.ToString());
                    cmd.Parameters.AddWithValue("@MQ", MedicineQuantityTb.Text);
                    cmd.Parameters.AddWithValue("@MP", MedicinePriceTb.Text);
                    cmd.Parameters.AddWithValue("@MMI", MedicineManfactCb.SelectedValue.ToString());
                    cmd.Parameters.AddWithValue("@MM", MedicineManfactNameTb.Text);
                    cmd.Parameters.AddWithValue("@Mkey", key);
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("Medicine Updated Successfully");



                    conn.Close();
                    ShowMed();
                    Reset();

                }
                catch (Exception Ex)
                {
                    MessageBox.Show(Ex.Message);
                }

            }


        }

        private void Medicines_Load(object sender, EventArgs e)
        {

        }

        private void label10_Click(object sender, EventArgs e)
        {
            Manufacturer obj = new Manufacturer();
            obj.Show();
            this.Hide();
        }

        private void label17_Click(object sender, EventArgs e)
        {
            Customer obj = new Customer();
            obj.Show();
            this.Hide();
        }

        private void label18_Click(object sender, EventArgs e)
        {
            Sellers obj = new Sellers();
            obj.Show();
            this.Hide();
        }

        private void label19_Click(object sender, EventArgs e)
        {
            Dashboard obj = new Dashboard();
            obj.Show();
            this.Hide();
        }

        private void label20_Click(object sender, EventArgs e)
        {
            Login loginForm = new Login();
            loginForm.Show();
            this.Close();
        }

        private void MedicineNameTb_TextChanged(object sender, EventArgs e)
        {

        }

        private void MedicineManfactNameTb_KeyPress(object sender, KeyPressEventArgs e)
        {

        }
    }
}
