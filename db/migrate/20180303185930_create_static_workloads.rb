class CreateStaticWorkloads < ActiveRecord::Migration[5.1]
  def change
    create_table :static_workloads do |t|
      t.integer :syllabus_id
      t.decimal :core, precision: 4, scale: 2
      t.decimal :assignments, precision: 4, scale: 2
      t.decimal :exams, precision: 4, scale: 2
      t.decimal :project, precision: 4, scale: 2

      t.timestamps
    end
  end
end
