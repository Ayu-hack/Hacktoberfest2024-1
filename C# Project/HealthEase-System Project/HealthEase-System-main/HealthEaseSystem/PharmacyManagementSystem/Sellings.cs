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
    public partial class Sellings : Form
    {
        public Sellings()
        {
            InitializeComponent();
            ShowMed();
            ShowBill();
            SNameLbl.Text = Login.User;
            GetCustomer();

        }

        SqlConnection conn = new SqlConnection(@"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\syedm\OneDrive\Documents\PharmacySystemDB.mdf;Integrated Security=True;Connect Timeout=30");
        private void label10_Click(object sender, EventArgs e)
        {

        }

        private void GetCustomer()
        {
            conn.Open();
            SqlCommand cmd = new SqlCommand("Select CustomerNum from CustomerTbl ", conn);
            SqlDataReader Rdr;
            Rdr = cmd.ExecuteReader();
            DataTable dt = new DataTable();
            dt.Columns.Add("CustomerNum", typeof(int));
            dt.Load(Rdr);
            CustIdCb.ValueMember = "CustomerNum";
            CustIdCb.DataSource = dt;

            conn.Close();
        }
        private void GetCustomerName()
        {
            conn.Open();
            string query = "Select * from CustomerTbl where CustomerNum='" + CustIdCb.SelectedValue.ToString() + "'";
            SqlCommand cmd = new SqlCommand(query, conn);
            DataTable dt = new DataTable();
            SqlDataAdapter sda = new SqlDataAdapter(cmd);
            sda.Fill(dt);
            foreach (DataRow dr in dt.Rows)
            {
                CustNameTb.Text = dr["CustomerName"].ToString();

            }


            conn.Close();
        }
        private void UpdateQty()
        {
            try
            {
                int NewQty = stock - Convert.ToInt32(MedicineQuantityTb.Text);
                conn.Open();
                SqlCommand cmd = new SqlCommand("Update MedicineTbl Set MedicineQuantity=@MQ where MedicineNum=@Mkey", conn);
                cmd.Parameters.AddWithValue("@MQ", NewQty);
                cmd.Parameters.AddWithValue("@Mkey", key);
                cmd.ExecuteNonQuery();
                MessageBox.Show("Medicine Updated Successfully");



                conn.Close();
                ShowMed();
               // Reset();

            }
            catch (Exception Ex)
            {
                MessageBox.Show(Ex.Message);
            }

        }
        private void InsertBill()
        {
            if(CustNameTb.Text == "")
            {
                MessageBox.Show("Customer name is required!!!");

            }
            else
            {

                try
                {
                    conn.Open();
                    
                     

                        SqlCommand cmd = new SqlCommand("insert into BillTbl(SellerName,CustomerNum,CustomerName,MedicineName,MedicineQuantity,MedicinePrice,BillDate,BillAmount)values(@SN,@CN,@CNa,@MN,@MQ,@MP,@BD,@BA)", conn);
                        cmd.Parameters.AddWithValue("@SN", SNameLbl.Text);
                        cmd.Parameters.AddWithValue("@CN", CustIdCb.SelectedValue.ToString());
                        cmd.Parameters.AddWithValue("@CNa", CustNameTb.Text);
                    cmd.Parameters.AddWithValue("@MN", MedicineNameTb.Text);
                    cmd.Parameters.AddWithValue("@MQ", MedicineQuantityTb.Text);
                    cmd.Parameters.AddWithValue("@MP", MedicinePriceTb.Text);
                    cmd.Parameters.AddWithValue("@BD", DateTime.Today.Date);
                        cmd.Parameters.AddWithValue("@BA", GrdTotal);
                  
                    cmd.ExecuteNonQuery();
                    
                    MessageBox.Show("BILL Saved Successfully");


                    conn.Close();
                    ShowBill();

                }
                catch (Exception Ex)
                {
                    MessageBox.Show(Ex.Message);
                }
            }
          

        }
        private void ShowBill()
        {
            conn.Open();
            string query = "Select * from BillTbl where SellerName='"+SNameLbl.Text+"'";
            SqlDataAdapter sda = new SqlDataAdapter(query, conn);
            SqlCommandBuilder Builder = new SqlCommandBuilder(sda);
            var ds = new DataSet();
            sda.Fill(ds);
            TransactionDGV.DataSource = ds.Tables[0];


            conn.Close();
        }

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

        private void Sellings_Load(object sender, EventArgs e)
        {

        }

        private void label8_Click(object sender, EventArgs e)
        {

        }
        int n = 0,GrdTotal=0;
        private void SaveBtn_Click(object sender, EventArgs e)
        {
            if(MedicineQuantityTb.Text== "" || Convert.ToInt32(MedicineQuantityTb.Text)>stock)
            {
                MessageBox.Show("Enter Correct Quantity");
            }
            else
            {
                int total = Convert.ToInt32(MedicineQuantityTb.Text) * Convert.ToInt32(MedicinePriceTb.Text);
                DataGridViewRow newRow = new DataGridViewRow();
                newRow.CreateCells(BillDGV);
                newRow.Cells[0].Value = n + 1;
                newRow.Cells[1].Value = MedicineNameTb.Text;
                newRow.Cells[2].Value = MedicineQuantityTb.Text;
                newRow.Cells[3].Value = MedicinePriceTb.Text;
                newRow.Cells[4].Value = total;
                BillDGV.Rows.Add(newRow);
                GrdTotal = GrdTotal + total;
                TotalLbl.Text = "RS  " +GrdTotal;
                n++;
                UpdateQty();


            }
        }

        int key = 0,stock;
        int MedId, Medprice, MedQty, MedTot;

        private void CustIdCb_SelectionChangeCommitted(object sender, EventArgs e)
        {
            GetCustomerName();
        }

        private void label20_Click(object sender, EventArgs e)
        {
            Login obj = new Login();
            obj.Show();
            this.Close();
        }

        private void label16_Click(object sender, EventArgs e)
        {
            //Medicines obj = new Medicines();
            //obj.Show();
            //this.Hide();
        }

        private void label18_Click(object sender, EventArgs e)
        {

        }

        private void label17_Click(object sender, EventArgs e)
        {

        }

        private void label10_Click_1(object sender, EventArgs e)
        {

        }

        private void label19_Click(object sender, EventArgs e)
        {

        }

        private void TransactionDGV_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void panel6_Paint(object sender, PaintEventArgs e)
        {

        }

        int pos = 60;

        private void PrintBtn_Click(object sender, EventArgs e)
        {
          
            printDocument1.DefaultPageSettings.PaperSize = new System.Drawing.Printing.PaperSize("pprnm",285,600);
            if(printPreviewDialog1.ShowDialog() == DialogResult.OK)
            {
                printDocument1.Print();
            }
            InsertBill();


        }
        string MedName;
        private void printDocument1_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
        {
            GrdTotal = 0;

            e.Graphics.DrawString("**PharmaPulse Pharmacy**", new Font("Century Gothic", 8, FontStyle.Bold), Brushes.Teal, new Point(80));
            e.Graphics.DrawString("ID MEDICINE PRICE QUANTITY TOTAL", new Font("Century Gothic", 9, FontStyle.Bold), Brushes.Teal, new Point(26, 40));

            foreach (DataGridViewRow row in BillDGV.Rows)
            {
                MedId = Convert.ToInt32(row.Cells["Column1"].Value);
                MedName = "" + row.Cells["Column2"].Value;
                Medprice = Convert.ToInt32(row.Cells["Column3"].Value);
                MedQty = Convert.ToInt32(row.Cells["Column4"].Value);
                MedTot = Convert.ToInt32(row.Cells["Column5"].Value);
                GrdTotal += MedTot;
                e.Graphics.DrawString("" + MedId, new Font("Century Gothic", 7, FontStyle.Bold), Brushes.Blue, new Point(26, pos));
                e.Graphics.DrawString("" + MedName, new Font("Century Gothic", 7, FontStyle.Bold), Brushes.Blue, new Point(45, pos));
                e.Graphics.DrawString("" + Medprice, new Font("Century Gothic", 7, FontStyle.Bold), Brushes.Blue, new Point(120, pos));
                e.Graphics.DrawString("" + MedQty, new Font("Century Gothic", 7, FontStyle.Bold), Brushes.Blue, new Point(170, pos));
                e.Graphics.DrawString("" + MedTot, new Font("Century Gothic", 7, FontStyle.Bold), Brushes.Blue, new Point(235, pos));
                pos = pos + 20;
            }

            e.Graphics.DrawString(" Grand Total: RS " + GrdTotal, new Font("Century Gothic", 11, FontStyle.Bold), Brushes.Teal, new Point(50, pos + 50));
            e.Graphics.DrawString("***👤👤 PharmaPulse Mart 👤👤***", new Font("Century Gothic", 11, FontStyle.Bold), Brushes.Teal, new Point(10, pos + 85));
            BillDGV.Rows.Clear();
            BillDGV.Refresh();
            pos = 100;
          //  GrdTotal = 0;
            n = 0;


        }


        private void MedicinesDGV_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            MedicineNameTb.Text = MedicinesDGV.SelectedRows[0].Cells[1].Value.ToString();
           // MedicineTypeCb.SelectedItem = MedicinesDGV.SelectedRows[0].Cells[2].Value.ToString();
           stock = Convert.ToInt32(MedicinesDGV.SelectedRows[0].Cells[3].Value.ToString());
            MedicinePriceTb.Text = MedicinesDGV.SelectedRows[0].Cells[4].Value.ToString();
           // MedicineManfactCb.SelectedValue = MedicinesDGV.SelectedRows[0].Cells[5].Value.ToString();
           // MedicineManfactNameTb.Text = MedicinesDGV.SelectedRows[0].Cells[6].Value.ToString();


            if (MedicineNameTb.Text == "")
            {
                key = 0;

            }
            else
            {
                key = Convert.ToInt32(MedicinesDGV.SelectedRows[0].Cells[0].Value.ToString());
            }
        }
    }
}
