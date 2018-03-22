class CreateSchedules < ActiveRecord::Migration[5.1]
  def change
    create_table :schedules do |t|
      t.string :semester
      t.string :day
      t.datetime :time
      t.boolean :project
      t.boolean :fieldwork
      t.integer :ratings

      t.timestamps
    end
  end
end
