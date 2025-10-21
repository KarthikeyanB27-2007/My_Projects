import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.io.*;

public class HospitalManagementSystemGUI extends JFrame {
    private java.util.List<Doctor> doctors = new ArrayList<>();
    private java.util.List<Patient> patients = new ArrayList<>();
    private JTable doctorTable, patientTable, appointmentTable;
    private DefaultTableModel doctorModel, patientModel, appointmentModel;
    private JTextField txtSearchDoctor;

    // Combos for appointments
    private JComboBox<String> cmbDoctorApp = new JComboBox<>();
    private JComboBox<String> cmbPatientApp = new JComboBox<>();

    // Combos for prescription
    private JComboBox<String> cmbDoctorPresc = new JComboBox<>();
    private JComboBox<String> cmbPatientPresc = new JComboBox<>();

    // Combo for Billing tab (global for refresh)
    private JComboBox<String> cmbBillingPatient = new JComboBox<>();

    public HospitalManagementSystemGUI() {
        setTitle("🏥 Hospital Management System");
        setSize(950, 700);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        JTabbedPane tabs = new JTabbedPane();
        tabs.addTab("Doctors", createDoctorPanel());
        tabs.addTab("Patients", createPatientPanel());
        tabs.addTab("Appointments", createAppointmentPanel());
        tabs.addTab("Prescription", createPrescriptionPanel());
        tabs.addTab("Billing", createBillingPanel());

        add(tabs);
    }

    // ------------------ Doctor Panel ------------------
    private JPanel createDoctorPanel() {
        JPanel panel = new JPanel(new BorderLayout());

        JPanel searchPanel = new JPanel(new BorderLayout());
        txtSearchDoctor = new JTextField();
        JButton btnSearchDoctor = new JButton("Search");
        searchPanel.add(new JLabel("🔍 Search Doctor: "), BorderLayout.WEST);
        searchPanel.add(txtSearchDoctor, BorderLayout.CENTER);
        searchPanel.add(btnSearchDoctor, BorderLayout.EAST);
        panel.add(searchPanel, BorderLayout.NORTH);

        String[] cols = {"Doctor Name", "Specialization", "Available Time"};
        doctorModel = new DefaultTableModel(cols, 0);
        doctorTable = new JTable(doctorModel);
        panel.add(new JScrollPane(doctorTable), BorderLayout.CENTER);

        JPanel form = new JPanel(new GridLayout(5,2,10,10));
        JTextField txtName = new JTextField();
        JTextField txtSpec = new JTextField();
        JTextField txtTime = new JTextField();
        JButton btnAdd = new JButton("Add Doctor");
        JButton btnEdit = new JButton("Edit Selected");
        JButton btnDelete = new JButton("Delete Selected");

        form.add(new JLabel("Doctor Name:")); form.add(txtName);
        form.add(new JLabel("Specialization:")); form.add(txtSpec);
        form.add(new JLabel("Available Time:")); form.add(txtTime);
        form.add(btnAdd); form.add(btnEdit);
        form.add(new JLabel("")); form.add(btnDelete);

        panel.add(form, BorderLayout.SOUTH);

        btnAdd.addActionListener(e -> {
            String name = txtName.getText(), spec = txtSpec.getText(), time = txtTime.getText();
            if(name.isEmpty() || spec.isEmpty() || time.isEmpty()){
                JOptionPane.showMessageDialog(this,"Please fill all fields!");
                return;
            }
            Doctor d = new Doctor(name, spec, time);
            doctors.add(d);
            doctorModel.addRow(new Object[]{name, spec, time});
            txtName.setText(""); txtSpec.setText(""); txtTime.setText("");

            refreshDoctorCombos();
        });

        btnEdit.addActionListener(e -> {
            int row = doctorTable.getSelectedRow();
            if(row>=0){
                Doctor d = doctors.get(row);
                d.name = txtName.getText(); d.specialization = txtSpec.getText(); d.time = txtTime.getText();
                doctorModel.setValueAt(d.name, row, 0);
                doctorModel.setValueAt(d.specialization, row, 1);
                doctorModel.setValueAt(d.time, row, 2);
                refreshDoctorCombos();
            }
        });

        btnDelete.addActionListener(e -> {
            int row = doctorTable.getSelectedRow();
            if(row>=0){
                doctors.remove(row);
                doctorModel.removeRow(row);
                refreshDoctorCombos();
            }
        });

        btnSearchDoctor.addActionListener(e -> {
            String query = txtSearchDoctor.getText().toLowerCase();
            if(query.isEmpty()) return;
            StringBuilder results = new StringBuilder();
            for(Doctor d : doctors){
                if(d.name.toLowerCase().contains(query) || d.specialization.toLowerCase().contains(query))
                    results.append(d.name).append(" - ").append(d.specialization).append("\n");
            }
            JOptionPane.showMessageDialog(this, results.length()>0 ? results.toString() : "No matching doctor found.");
        });

        return panel;
    }

    // ------------------ Patient Panel ------------------
    private JPanel createPatientPanel() {
        JPanel panel = new JPanel(new BorderLayout());

        String[] cols = {"Patient Name","Age","Disease","Type"};
        patientModel = new DefaultTableModel(cols,0);
        patientTable = new JTable(patientModel);
        panel.add(new JScrollPane(patientTable), BorderLayout.CENTER);

        JPanel form = new JPanel(new GridLayout(6,2,10,10));
        JTextField txtName = new JTextField();
        JTextField txtAge = new JTextField();
        JTextField txtDisease = new JTextField();
        JButton btnAdd = new JButton("Add Patient");
        JButton btnEdit = new JButton("Edit Selected");
        JButton btnDelete = new JButton("Delete Selected");
        JButton btnCheckType = new JButton("Check Outpatient/New Patient");

        form.add(new JLabel("Patient Name:")); form.add(txtName);
        form.add(new JLabel("Age:")); form.add(txtAge);
        form.add(new JLabel("Disease:")); form.add(txtDisease);
        form.add(btnAdd); form.add(btnEdit);
        form.add(new JLabel("")); form.add(btnDelete);
        form.add(new JLabel("")); form.add(btnCheckType);

        panel.add(form, BorderLayout.SOUTH);

        JPanel searchPanel = new JPanel(new BorderLayout());
        JTextField txtSearchPatient = new JTextField();
        JButton btnSearchPatient = new JButton("Search Patient");
        searchPanel.add(new JLabel("🔍 Search Patient: "), BorderLayout.WEST);
        searchPanel.add(txtSearchPatient, BorderLayout.CENTER);
        searchPanel.add(btnSearchPatient, BorderLayout.EAST);
        panel.add(searchPanel, BorderLayout.NORTH);

        btnAdd.addActionListener(e -> {
            String name = txtName.getText(), age = txtAge.getText(), disease = txtDisease.getText();
            if(name.isEmpty() || age.isEmpty() || disease.isEmpty()){
                JOptionPane.showMessageDialog(this,"Please fill all fields!");
                return;
            }
            String type = Integer.parseInt(age)>50?"Outpatient":"New Patient";
            Patient p = new Patient(name, age, disease, type);
            patients.add(p);
            patientModel.addRow(new Object[]{name, age, disease, type});
            txtName.setText(""); txtAge.setText(""); txtDisease.setText("");

            refreshPatientCombos();
            refreshPatientCombos(cmbBillingPatient);
        });

        btnEdit.addActionListener(e -> {
            int row = patientTable.getSelectedRow();
            if(row>=0){
                Patient p = patients.get(row);
                p.name = txtName.getText(); p.age = txtAge.getText(); p.disease = txtDisease.getText();
                p.type = Integer.parseInt(p.age)>50?"Outpatient":"New Patient";
                patientModel.setValueAt(p.name,row,0);
                patientModel.setValueAt(p.age,row,1);
                patientModel.setValueAt(p.disease,row,2);
                patientModel.setValueAt(p.type,row,3);
                refreshPatientCombos();
                refreshPatientCombos(cmbBillingPatient);
            }
        });

        btnDelete.addActionListener(e -> {
            int row = patientTable.getSelectedRow();
            if(row>=0){
                patients.remove(row);
                patientModel.removeRow(row);
                refreshPatientCombos();
                refreshPatientCombos(cmbBillingPatient);
            }
        });

        btnCheckType.addActionListener(e -> {
            int row = patientTable.getSelectedRow();
            if(row>=0){
                Patient p = patients.get(row);
                JOptionPane.showMessageDialog(this,p.name + " is a " + p.type);
            }
        });

        btnSearchPatient.addActionListener(e -> {
            String query = txtSearchPatient.getText().toLowerCase();
            StringBuilder results = new StringBuilder();
            for(Patient p:patients){
                if(p.name.toLowerCase().contains(query) || p.disease.toLowerCase().contains(query))
                    results.append(p.name).append(" - ").append(p.disease).append(" (").append(p.type).append(")\n");
            }
            JOptionPane.showMessageDialog(this, results.length()>0?results.toString():"No matching patient found.");
        });

        return panel;
    }

    // ------------------ Appointments Tab ------------------
    private JPanel createAppointmentPanel() {
        JPanel panel = new JPanel(new BorderLayout());

        String[] cols = {"Doctor","Patient","Time"};
        appointmentModel = new DefaultTableModel(cols,0);
        appointmentTable = new JTable(appointmentModel);
        panel.add(new JScrollPane(appointmentTable), BorderLayout.CENTER);

        JPanel form = new JPanel(new GridLayout(4,2,10,10));
        JTextField txtTime = new JTextField();
        JButton btnAdd = new JButton("Add Appointment");

        form.add(new JLabel("Doctor:")); form.add(cmbDoctorApp);
        form.add(new JLabel("Patient:")); form.add(cmbPatientApp);
        form.add(new JLabel("Time:")); form.add(txtTime);
        form.add(new JLabel("")); form.add(btnAdd);
        panel.add(form, BorderLayout.SOUTH);

        btnAdd.addActionListener(e -> {
            String doctor = (String)cmbDoctorApp.getSelectedItem();
            String patient = (String)cmbPatientApp.getSelectedItem();
            String time = txtTime.getText();
            if(doctor==null || patient==null || time.isEmpty()){
                JOptionPane.showMessageDialog(this,"Fill all fields!");
                return;
            }
            appointmentModel.addRow(new Object[]{doctor, patient, time});
        });

        refreshDoctorCombos();
        refreshPatientCombos();

        return panel;
    }

    // ------------------ Prescription Tab ------------------
    private JPanel createPrescriptionPanel() {
        JPanel panel = new JPanel(new BorderLayout());
        JPanel inputPanel = new JPanel(new GridLayout(5,2,10,10));

        JTextArea txtMedicines = new JTextArea(3,20);
        txtMedicines.setEditable(false);
        JButton btnSave = new JButton("Save Prescription");

        String[] diseases = {"Fever","Cold","Headache","Cough","Diabetes","BP","Asthma","Allergy"};

        Map<String,String> medicineMap = new HashMap<>();
        medicineMap.put("Fever","Paracetamol 500mg, Dolo 650, Crocin");
        medicineMap.put("Cold","Cetirizine, Cofsils, Steam Inhalation");
        medicineMap.put("Headache","Aspirin, Ibuprofen, Saridon");
        medicineMap.put("Cough","Benadryl, Ascoril, Dextromethorphan Syrup");
        medicineMap.put("Diabetes","Metformin, Glibenclamide, Insulin");
        medicineMap.put("BP","Amlodipine, Atenolol, Lisinopril");
        medicineMap.put("Asthma","Salbutamol Inhaler, Montelukast, Budesonide");
        medicineMap.put("Allergy","Loratadine, Cetirizine, Allegra");

        JComboBox<String> cmbDisease = new JComboBox<>();
        for(String d:diseases) cmbDisease.addItem(d);

        cmbDisease.addActionListener(e -> {
            String disease = (String)cmbDisease.getSelectedItem();
            txtMedicines.setText(medicineMap.getOrDefault(disease,"No medicines available."));
        });

        inputPanel.add(new JLabel("Doctor:")); inputPanel.add(cmbDoctorPresc);
        inputPanel.add(new JLabel("Patient:")); inputPanel.add(cmbPatientPresc);
        inputPanel.add(new JLabel("Disease:")); inputPanel.add(cmbDisease);
        inputPanel.add(new JLabel("Medicines:")); inputPanel.add(new JScrollPane(txtMedicines));
        inputPanel.add(new JLabel("")); inputPanel.add(btnSave);

        panel.add(inputPanel, BorderLayout.CENTER);

        btnSave.addActionListener(e -> {
            String doctor = (String)cmbDoctorPresc.getSelectedItem();
            String patient = (String)cmbPatientPresc.getSelectedItem();
            String disease = (String)cmbDisease.getSelectedItem();
            String medicines = txtMedicines.getText();
            if(doctor==null || patient==null || disease==null || medicines.isEmpty()){
                JOptionPane.showMessageDialog(this,"Please fill all fields.");
                return;
            }
            try(FileWriter fw = new FileWriter("prescriptions.txt",true)){
                fw.write("Doctor: "+doctor+"\nPatient: "+patient+"\nDisease: "+disease+"\nMedicines: "+medicines+"\n-----------------------------\n");
                JOptionPane.showMessageDialog(this,"Prescription saved to prescriptions.txt");
            } catch(Exception ex){
                JOptionPane.showMessageDialog(this,"Error saving prescription!");
            }
        });

        refreshDoctorCombos();
        refreshPatientCombos();

        return panel;
    }

    // ------------------ Billing Tab ------------------
    private JPanel createBillingPanel() {
        JPanel panel = new JPanel(new BorderLayout());
        JPanel inputPanel = new JPanel(new BorderLayout(10,10));

        // Use class/global patient combo box
        refreshPatientCombos(cmbBillingPatient);

        String[] cols = {"Medicine","Price (₹)"};
        DefaultTableModel billModel = new DefaultTableModel(cols,0);
        JTable billTable = new JTable(billModel);
        JScrollPane scrollPane = new JScrollPane(billTable);

        JButton btnCalc = new JButton("Calculate Total");
        JButton btnSave = new JButton("Save Bill");
        JLabel lblTotal = new JLabel("Total: ₹0.00", SwingConstants.CENTER);

        // Disease and medicines map
        Map<String, String> medicineRates = new HashMap<>();
        medicineRates.put("Fever","Paracetamol:50,Dolo:60,Crocin:45");
        medicineRates.put("Cold","Cetirizine:30,Cofsils:20,SteamInhalation:0");
        medicineRates.put("Headache","Aspirin:25,Ibuprofen:35,Saridon:40");
        medicineRates.put("Cough","Benadryl:45,Ascoril:50,Dextromethorphan:55");
        medicineRates.put("Diabetes","Metformin:100,Glibenclamide:120,Insulin:200");
        medicineRates.put("BP","Amlodipine:90,Atenolol:85,Lisinopril:110");
        medicineRates.put("Asthma","Salbutamol:70,Montelukast:60,Budesonide:80");
        medicineRates.put("Allergy","Loratadine:40,Cetirizine:30,Allegra:50");

        // Auto-populate medicine rates on patient selection
        cmbBillingPatient.addActionListener(e -> {
            int selectedIndex = cmbBillingPatient.getSelectedIndex();
            if(selectedIndex<0 || selectedIndex>=patients.size()) return;
            Patient p = patients.get(selectedIndex);
            billModel.setRowCount(0);
            String meds = medicineRates.getOrDefault(p.disease,"");
            if(!meds.isEmpty()){
                String[] arr = meds.split(",");
                for(String s:arr){
                    String[] parts = s.split(":");
                    billModel.addRow(new Object[]{parts[0], parts[1]});
                }
            }
        });

        JPanel top = new JPanel(new FlowLayout(FlowLayout.LEFT, 10, 10));
        top.add(new JLabel("Select Patient:"));
        top.add(cmbBillingPatient);

        inputPanel.add(top, BorderLayout.NORTH);
        inputPanel.add(scrollPane, BorderLayout.CENTER);
        inputPanel.add(lblTotal, BorderLayout.SOUTH);

        panel.add(inputPanel, BorderLayout.CENTER);
        panel.add(btnCalc, BorderLayout.WEST);
        panel.add(btnSave, BorderLayout.EAST);

        btnCalc.addActionListener(e -> {
            double total = 0;
            for(int i=0;i<billModel.getRowCount();i++){
                try{ total += Double.parseDouble(billModel.getValueAt(i,1).toString()); } catch(Exception ignored){}
            }
            lblTotal.setText("Total: ₹"+total);
        });

        btnSave.addActionListener(e -> {
            int idx = cmbBillingPatient.getSelectedIndex();
            if(idx<0 || billModel.getRowCount()==0){
                JOptionPane.showMessageDialog(this,"Select patient with items before saving!");
                return;
            }
            Patient p = patients.get(idx);
            try(FileWriter fw = new FileWriter("bills.txt",true)){
                fw.write("Patient: "+p.name+"\nDisease: "+p.disease+"\n");
                double total=0;
                for(int i=0;i<billModel.getRowCount();i++){
                    String med = billModel.getValueAt(i,0).toString();
                    double price = Double.parseDouble(billModel.getValueAt(i,1).toString());
                    fw.write(" - "+med+": ₹"+price+"\n");
                    total+=price;
                }
                fw.write("Total: ₹"+total+"\n-----------------------------\n");
                JOptionPane.showMessageDialog(this,"Bill saved to bills.txt");
            } catch(Exception ex){ JOptionPane.showMessageDialog(this,"Error saving bill!"); }
        });

        return panel;
    }

    // ------------------ Helper Methods ------------------
    private void refreshDoctorCombos(){
        cmbDoctorApp.removeAllItems();
        cmbDoctorPresc.removeAllItems();
        for(Doctor d:doctors){
            cmbDoctorApp.addItem(d.name);
            cmbDoctorPresc.addItem(d.name);
        }
    }
    private void refreshPatientCombos(){
        cmbPatientApp.removeAllItems();
        cmbPatientPresc.removeAllItems();
        for(Patient p:patients){
            cmbPatientApp.addItem(p.name);
            cmbPatientPresc.addItem(p.name);
        }
        refreshPatientCombos(cmbBillingPatient); // keep billing ComboBox in sync too
    }
    private void refreshPatientCombos(JComboBox<String> cmb){
        cmb.removeAllItems();
        for(Patient p:patients) cmb.addItem(p.name);
    }

    // ------------------ Classes ------------------
    static class Doctor{
        String name,specialization,time;
        Doctor(String n,String s,String t){ name=n; specialization=s; time=t; }
    }
    static class Patient{
        String name,age,disease,type;
        Patient(String n,String a,String d,String t){ name=n; age=a; disease=d; type=t; }
    }

    // ------------------ Main ------------------
    public static void main(String[] args){
        SwingUtilities.invokeLater(() -> new HospitalManagementSystemGUI().setVisible(true));
    }
}
