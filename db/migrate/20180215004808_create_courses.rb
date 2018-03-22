class CreateCourses < ActiveRecord::Migration[5.1]
  def change
    create_table :courses do |t|
      t.integer :code
      t.integer :syllabus_id
      t.string :prerequisites
      t.string :course_name
      t.string :description
      t.boolean :core
      t.integer :channel_id

      t.timestamps
    end
  end
end
